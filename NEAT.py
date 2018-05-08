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
# import Pitfall_ram
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

        nodes.append(NodeGene(nodeNum = numInputs + numY + 1, t = 'Hidden', layer = 1))
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


        connections.append(ConnectGene(x = 1, Y = numInputs + numY + 1, weight = random.randrange(-100, 100, 1), enabled = True, innovation=population.innovationCounter))
        connections.append(ConnectGene(x = 2, Y = numInputs + numY + 1, weight = random.randrange(-100, 100, 1), enabled = True, innovation=population.innovationCounter + 1))
        connections.append(ConnectGene(x = 3, Y = numInputs + numY + 1, weight = random.randrange(-100, 100, 1), enabled = True, innovation=population.innovationCounter + 2))

        connections.append(ConnectGene(x = numInputs + numY + 1, Y = 4 , weight = random.randrange(-100, 100, 1), enabled = True, innovation=population.innovationCounter + 3))
        population.currentPop.append(Genome(connections = connections, nodes = nodes))

    population.currentPop = [population.currentPop]
    population.species.append(Species(epochs=0, allowed_offspring=popCap))
    population.maxNodes = numInputs + numY


def inbreed():

    for species_index, listy in enumerate(population.currentPop):
        reproduced = 0

        if len(listy) >= 5:
            next_gen.currentPop.append(copy.deepcopy(listy[0]))
            reproduced += 1

        if len(listy) > 5:
            for _ in range(int(round(len(listy) * .2))):
                del listy[-1]

        # for gnome in iter_pop:
        for gnome in listy:
            if len(listy) > 2:
                inbred_genome = (crossbreed(gnome, random.choice(listy)))
            else:
                inbred_genome = copy.deepcopy(gnome)


            #   There needs to be a greater chance of adding a connection than a new node
            if len(listy) == 1:
                next_gen.currentPop.append(inbred_genome)
            elif random.random() < .005: # with smaller populations .03 was used in the paper.
                next_gen.mutate_add_node(inbred_genome)
            elif random.random() < .01: # the probability of adding a new link will be .05 for smaller populations
                next_gen.mutate_add_connection(inbred_genome)
            elif random.random() < .8:  # 80% chance of having is connection weights mutated
                next_gen.mutate_weight(inbred_genome)

            # TODO interspecies crossbreeding rate will be .001

            # TODO the probability of adding a new link will be .05 for smaller populations
            #   with larger populations it was .03 because they can handle greater diversity.
            #   this seems like a typo but i cross checked the paper.
            reproduced += 1
            if reproduced > population.species[species_index].allowed_offspring:
                break
            next_gen.currentPop.append(inbred_genome)

        # being lazy here, need to refactor.
        while reproduced < population.species[species_index].allowed_offspring:
            if len(listy) > 2:
                inbred_genome = (crossbreed(random.choice(listy), random.choice(listy)))
            else:
                inbred_genome = copy.deepcopy(gnome)

            if random.random() < .005: # default is .03
                next_gen.mutate_add_node(inbred_genome)
            elif random.random() < .01: # the probability of adding a new link will be .05 for smaller populations
                next_gen.mutate_add_connection(inbred_genome)
            elif random.random() < .8:  # 80% chance of having is connection weights mutated
                next_gen.mutate_weight(inbred_genome)

            reproduced += 1
            next_gen.currentPop.append(inbred_genome)


def speciate():
    representatives = []
    for listy in population.currentPop:
        representatives.append(random.choice(listy))

    next_species = [[] for _ in range(len(representatives))]
    for genome in next_gen.currentPop:
        for index, representative in enumerate(representatives):
            if get_delta(genome, representative) < population.delta_threshold:
                next_species[index].append(genome)
                break

            elif index == len(representatives) - 1:
                representatives.append(genome)
                next_species.append([genome])
                population.species.append(Species(epochs=0, stagnant=0))
                break

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


def update_species_info():
    to_delete = []
    for index, species in enumerate(population.species):
        population.currentPop[index].sort(key=lambda x: x.fitness, reverse=True)

        if species.max_fitness < population.currentPop[index][0].fitness:
            species.max_fitness = population.currentPop[index][0].fitness
        elif species.epochs_lived is not 0:
            species.epochs_stagnant += 1

        species.epochs_lived += 1

        if species.epochs_stagnant == 10 and population.currentPop[index][0].fitness < min_fitness_to_keep_living:
            print("u_s_i(), max fitness deleted", population.currentPop[index][0].fitness)
            to_delete.append(index)

    if len(to_delete) == len(population.currentPop):
        for speciess in population.species:
            speciess.epochs_stagnant = 5
    else:
        list.reverse(to_delete)
        for index in to_delete:
            del population.species[index]
            del population.currentPop[index]


if '__main__' == __name__:
    # game = XOR
    game = MountainCar
    # game = cartpole
    # game = Pitfall_ram
    """
    4 for xor
    -110 for MountainCar
    200 for cartpole
    """
    min_fitness_to_keep_living = -110
    popCap = 10
    population = Population()
    numInputs, numY = game.get_xy()
    numY = int(numY)
    generate_initial_population()

    for i in range(30):
        next_gen = Population()
        print("\nmain(), epoch:", i + 1)
        print("main(), num species", len(population.currentPop))
        print("main(), num species:", len(population.species))

        next_gen.maxNodes = population.maxNodes
        next_gen.innovationCounter = population.innovationCounter
        next_gen.connectionList = population.connectionList
        next_gen.pair = population.pair
        next_gen.species = population.species



        for species in next_gen.species:
            species.allowed_offspring = int(round(popCap / len(next_gen.species)))

        inbreed()
        speciate()
        population = next_gen
        run_game()
        update_species_info()
        population.calc_pop_adjusted_fitness()
        for i, x in enumerate(population.currentPop):
            print("main(): species " + str(i) + " champion has a fitness of " +
                  str(population.currentPop[i][0].fitness))

    print("____________________Population Fitness__________________________")
    print("main(), num species", len(population.currentPop))
    sum = 0

    for species_num, listy in enumerate(population.currentPop):
        print("main(), species num: " + str(species_num + 1) + ", num genomes: " + str(len(listy)))
        print("main(), fitness of champion:", listy[0].fitness)
        print("main(), num nodes in champion:", len(listy[0].nodes))
        input("press key to render game")
        game.render_game(listy[0])
