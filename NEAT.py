# This is where most if not all of the GA and NEAT logic will happen.
import copy
import random
import gc
import sys
import time

from ConnectGene import ConnectGenes
from Genome import Genome
from NodeGene import NodeGenes
from Population import Population
from Config import Config
from BuildNeuralNet import NeuralNet
from Population import crossbreed


import cartpole
import MountainCar
from misc.Json import to_json

population = Population()


def generate_initial_population():
    global population
    population = Population()
    for _ in range(popCap):
        nodes = []
        for i in range(1, numInputs + 1):
            nodes.append(NodeGenes(nodeNum = i, t = 'Sensor', layer = float('-inf')))
        for i in range(1, numY + 1):
            nodes.append(NodeGenes(nodeNum = numInputs + i, t = 'Output', layer = float('inf')))

        connections = []

        for i in range(1, numInputs + 1):
            for j in range(numInputs + 1, numInputs + numY + 1):
                innovation = None
                if any(x.x == i and x.Y == j for x in population.connectionList):
                    innovation = [z for z,x in enumerate(population.connectionList) if x.x == i and x.Y == j][0]
                else:
                    innovation = population.innovationCounter
                    population.innovationCounter += 1
                    population.connectionList.append(ConnectGenes(x = i, Y = j, innovation = innovation))
                connections.append(ConnectGenes(x = i, Y = j, weight = random.randrange(-100, 100, 1), enabled = True, innovation=innovation))

        population.currentPop.append(Genome(connections = connections, nodes = nodes))

    population.maxNodes = numInputs + numY + 1


def inbreed():

    # Elitism is working with this implementation, it may not look like it when the code is ran, that is because
    #   our best genome cant handle every situation in cartpole.
    for gnome in range(int(round(.1 * popCap))):
        # next_gen.currentPop.append(copy.deepcopy(population.currentPop[gnome]))
        next_gen.currentPop.append(population.currentPop[gnome])

    for gnome in range(int(round(.9 * popCap))):
        inbred_genome = (crossbreed(population.currentPop[gnome],
                         random.choice(population.currentPop[:popCap - int(round(popCap * .8))])))
        chance = random.random()

        # not sure if this is the proper way of doing chances.

        # with smaller populations .03 was used in the paper.
        #   There needs to be a greater chance of adding a connection than a new node
        if chance < .03:
            next_gen.mutate_add_node(inbred_genome)
        elif chance < .8:  # 80% chance of having is connection weights mutated
            next_gen.mutate_weight(inbred_genome)
        # TODO interspecies crossbreeding rate will be .001

        # TODO the probability of adding a new link will be .05 for smaller populations
        #   with larger populations it was .03 because they can handle greater diversity.
        #   this seems like a typo but i cross checked the paper.
        next_gen.currentPop.append(inbred_genome)


def run_game():
    for i in range(len(population.currentPop)):
        neuralNet = NeuralNet(population.currentPop[i])
        try:
            neuralNet.build_neural_net()
        except Exception as e:
            print("Entered Exception block")
            print("key", e)
            print(population.currentPop[i])
            sys.exit()

        population.currentPop[i].fitness = game.get_fitness(neuralNet)


if '__main__' == __name__:
    game = MountainCar
    # game = cartpole
    popCap = 100
    population = Population()
    # next_gen = Population()
    numInputs, numY = game.get_xy()
    numY = int(numY)
    generate_initial_population()

    population.currentPop.sort(key = lambda x: x.fitness, reverse = True)

    for i in range(40):

        next_gen = Population()
        # print(len(population.currentPop))

        run_game()

        population.currentPop.sort(key = lambda x: x.fitness, reverse = True)
        # game.render_game(population.currentPop[0])
        next_gen.maxNodes = population.maxNodes
        next_gen.innovationCounter = population.innovationCounter

        next_gen.connectionList = copy.deepcopy(population.connectionList)
        start_time = time.time()
        inbreed()

        population = next_gen
        print("\nepoch:", i + 1)
        print("con length", len(population.connectionList))
        # print("winner con length", len(population.currentPop[0].connections))
        print("fitness:", population.currentPop[0].fitness)
        # to_json(population.currentPop[0])

    # print("_____________________Connection list___________________")
    # for con in range (len(next_gen.connectionList)):
    #     print(next_gen.connectionList[con])


    # while True:
