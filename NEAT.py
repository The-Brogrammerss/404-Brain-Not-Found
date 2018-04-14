# This is where most if not all of the GA and NEAT logic will happen.
import copy
import random
import gc
import sys
import time
import numpy as np

from ConnectGene import ConnectGene
from Genome import Genome
from NodeGene import NodeGene
from Population import Population
from Config import Config
from BuildNeuralNet import NeuralNet
from Population import crossbreed
from Population import get_delta
from Species import Species


import cartpole
import MountainCar
import XOR
from misc.Json import to_json

population = Population()


def generate_initial_population():
    global population
    population = Population()
    for _ in range(popCap):
        nodes = []
        for i in range(1, numInputs + 1):
            nodes.append(NodeGene(nodeNum = i, t ='Sensor', layer = float('-inf')))
        for i in range(1, numY + 1):
            nodes.append(NodeGene(nodeNum =numInputs + i, t ='Output', layer = float('inf')))

        connections = []

        for i in range(1, numInputs + 1):
            for j in range(numInputs + 1, numInputs + numY + 1):
                innovation = None
                if any(x.x == i and x.Y == j for x in population.connectionList):
                    innovation = [z for z,x in enumerate(population.connectionList) if x.x == i and x.Y == j][0]
                else:
                    innovation = population.innovationCounter
                    population.innovationCounter += 1
                    population.connectionList.append(ConnectGene(x = i, Y = j, innovation = innovation))
                connections.append(ConnectGene(x = i, Y = j, weight = random.randrange(-100, 100, 1), enabled = True, innovation=innovation))

        population.currentPop.append(Genome(connections = connections, nodes = nodes))

    population.currentPop = [population.currentPop]
    population.species.append(Species(epochs=0))
    population.maxNodes = numInputs + numY + 1


def inbreed():

    # Elitism is working with this implementation, it may not look like it when the code is ran, that is because
    #   our best genome cant handle every situation in cartpole.
    for listy in population.currentPop:
        iter_pop = iter(listy)
        if len(listy) >= 5:
            next_gen.currentPop.append(next(iter_pop))

        for gnome in iter_pop:
            if len(listy) > 2:
                inbred_genome = (crossbreed(gnome,
                                 random.choice(listy[:len(listy) - int(round(len(listy) * .8))])))
            else:
                inbred_genome = gnome

            # with smaller populations .03 was used in the paper.
            #   There needs to be a greater chance of adding a connection than a new node
            if random.random() < .03:
                next_gen.mutate_add_node(inbred_genome)
            elif random.random() < .05: # the probability of adding a new link will be .05 for smaller populations
                next_gen.mutate_add_connection(inbred_genome)
            elif random.random() < .8:  # 80% chance of having is connection weights mutated
                next_gen.mutate_weight(inbred_genome)

            # TODO interspecies crossbreeding rate will be .001

            # TODO the probability of adding a new link will be .05 for smaller populations
            #   with larger populations it was .03 because they can handle greater diversity.
            #   this seems like a typo but i cross checked the paper.
            next_gen.currentPop.append(inbred_genome)


def speciate():
    species = []
    for listy in population.currentPop:
        species.append(random.choice(listy))

    next_species = [[] for _ in range(len(species))]

    for genome in next_gen.currentPop:
        for index, representative in enumerate(species):
            # print("delta:", get_delta(genome, representative))
            if get_delta(genome, representative) < population.delta_threshold:
                # print("below threshold")
                next_species[index].append(genome)
                break

            elif index == len(species) - 1:
                # print("above threshold")
                species.append(genome)
                next_species.append([genome])
                population.species.append(Species(epochs=0))
                break

    # TODO im going to remove any empty lists here we are going to have to remember to blow off that species object also
    to_delete = []
    for index, listy in enumerate(next_species):
        if len(listy) == 0:
            to_delete.append(index)
    list.reverse(to_delete)
    for index in to_delete:
        del population.species[index]
        del next_species[index]


    # next_species[:] = [listy for listy in next_species if len(listy) != 0]  # I remove all empty lists

    next_gen.currentPop = next_species


def run_game():
    for species in population.currentPop:
        for genome in species:
            neuralNet = NeuralNet(genome)
            try:
                neuralNet.build_neural_net()
            except Exception as e:
                print("Entered Exception block")
                print("key", e)
                print(genome)
                sys.exit()

            genome.fitness = game.get_fitness(neuralNet)


if '__main__' == __name__:
    game = XOR
    # game = MountainCar
    # game = cartpole
    popCap = 100
    population = Population()
    # next_gen = Population()
    numInputs, numY = game.get_xy()
    numY = int(numY)
    generate_initial_population()
    run_game()
    for listy in population.currentPop:
        listy.sort(key = lambda x: x.fitness, reverse = True)


    for i in range(2):
        next_gen = Population()
        print("\nmain(), epoch:", i + 1)
        print("main(), len(cur_pop):", len(population.currentPop))
        print("main(), num species:", len(population.species))

        next_gen.maxNodes = population.maxNodes
        next_gen.innovationCounter = population.innovationCounter
        next_gen.connectionList = population.connectionList
        next_gen.pair = population.pair
        next_gen.species = population.species

        inbreed()
        speciate()

        population = next_gen
        run_game()
        for listy in population.currentPop:
            listy.sort(key=lambda x: x.fitness, reverse=True)

        population.calc_pop_adjusted_fitness()
        for listy in population.currentPop:
            for genome in listy:
                print("main(), adjusted fitness", genome.adjusted_fitness)
        #print("\nepoch:", i + 1)
        #print("con length", len(population.connectionList))
        # print("winner con length", len(population.currentPop[0].connections))
        #print("fitness:", population.currentPop[0].fitness)
        # if i == 0:
        #     old_fitness = population.currentPop[0].fitness
        # if population.currentPop[0].fitness > old_fitness + 5:
        #     #game.render_game(population.currentPop[0])
        #     old_fitness = population.currentPop[0].fitness
        # to_json(population.currentPop[0])


    print("____________________Population Fitness__________________________")
    print("main(), num species", len(population.currentPop))
    sum = 0
    for listy in population.currentPop:
        sum += len(listy)
        listy.sort(key=lambda x: x.fitness, reverse=True)
    print("main(), num genomes", sum)
    for species_num, listy in enumerate(population.currentPop):
        print("main(), species num: " + str(species_num + 1) + ", num genomes: " + str(len(listy)))
        print("main(), fitness of champion:", listy[0].fitness)
        # for guy in listy:
        #     print("fitness:", guy.fitness)

    # for guy in population.currentPop:
    #     #print(guy)
    #     pass
    # input("play last genome hit key")
    #game.render_game(population.currentPop[0])
    # print("_____________________Connection list___________________")
    # for con in range (len(next_gen.connectionList)):
    #     print(next_gen.connectionList[con])
