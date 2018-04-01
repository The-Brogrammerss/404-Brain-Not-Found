# This is where most if not all of the GA and NEAT logic will happen.
import copy
import random
import gc
import sys
import time

from ConnectGenes import ConnectGenes
from Genome import Genome
from NodeGenes import NodeGenes
from Population import Population
from Config import Config
from BuildNeuralNet import NeuralNet
from Population import crossbreed

import cartpole
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


# def copy_to_popCap(gnome):
#     for i in range(1, popCap):
#         g = copy.deepcopy(gnome)
#         for k in range(len(g.connections)):
#             g.connections[k].weight = random.randrange(-100, 100, 1)
#         population.currentPop.append(g)

#
# def generate_connections(gnome):
#     for k in range(0, len(gnome.nodes)):
#         if gnome.nodes[k].type == "Sensor":
#             for j in range(1, len(gnome.nodes)):
#                 if gnome.nodes[j].type == "Output":
#                     cons = ConnectGenes()
#                     cons.x = gnome.nodes[k].nodeNum
#                     cons.Y = gnome.nodes[j].nodeNum
#                     cons.enabled = True
#                     population.innovationCounter = population.innovationCounter + 1
#                     cons.innovation = population.innovationCounter
#                     cons.weight = random.randrange(Config.dict["min_weight"],
#                                                    100, 1)
#                     gnome.connections.append(cons)
#                     population.connectionList.append(cons)


def git_gud():

    for gnome in range(int(round(.1 * popCap))):
        # next_gen.currentPop.append(copy.deepcopy(population.currentPop[gnome]))
        next_gen.currentPop.append(population.currentPop[gnome])


    start_time = time.time()
    for gnome in range(int(round(.9 * popCap))):
        next_gen.currentPop.append(crossbreed(population.currentPop[gnome],
                                              random.choice(population.currentPop[:popCap])))
    print("time", time.time() - start_time)
    start_time = time.time()
    for gnome in range(int(round(.4 * popCap))):
        next_gen.mutate_weight(gnome)
    print("time", time.time() - start_time)
    start_time = time.time()
    for gnome in range(int(round(.01 * popCap))):
        next_gen.mutate_add_node(random.randint(0, popCap - 1))
    # next_gen.mutate_add_node(random.choice(population.currentPop[:popCap]))
    print("time", time.time() - start_time)



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

        population.currentPop[i].fitness = cartpole.get_fitness(neuralNet)


if '__main__' == __name__:
    popCap = 100
    population = Population()
    # next_gen = Population()
    numInputs, numY = cartpole.get_xy()
    numY = int(numY)
    generate_initial_population()

    population.currentPop.sort(key = lambda x: x.fitness, reverse = True)

    for i in range(30):

        next_gen = Population()
        print(len(population.currentPop))

        run_game()

        population.currentPop.sort(key = lambda x: x.fitness, reverse = True)
        # cartpole.render_game(population.currentPop[0])
        # MountainCar.render_game(population.currentPop[0])
        next_gen.maxNodes = population.maxNodes
        next_gen.innovationCounter = population.innovationCounter

        next_gen.connectionList = copy.deepcopy(population.connectionList)
        start_time = time.time()
        git_gud()

        population = next_gen
        print("\nepoch:", i)
        print("con length", len(population.connectionList))
        # print("winner con length", len(population.currentPop[0].connections))
        print("fitness:", population.currentPop[0].fitness)
        # to_json(population.currentPop[0])

    print("_____________________Connection list___________________")
    for con in range (len(next_gen.connectionList)):
        print(next_gen.connectionList[con])

    print(population.currentPop[99])
    # while True:
