# This is where most if not all of the GA and NEAT logic will happen.
import copy
import random
import gc
from time import clock

from ConnectGenes import ConnectGenes
from Genome import Genome
from NodeGenes import NodeGenes
from Population import Population
from Config import Config
from BuildNeuralNet import NeuralNet

import cartpole
from misc.Json import to_json

population = Population()

def generate_initial_population():
    global population
    population = Population()
    for _ in range(popCap):
        nodes = []
        for i in range(1, numInputs + 1):
            nodes.append(NodeGenes(nodeNum = i, t = 'Sensor'))
        for i in range(1, numY + 1):
            nodes.append(NodeGenes(nodeNum = numInputs + i, t = 'Output'))

        connections = []
        for i in range(1, numInputs + 1):
            for j in range(numInputs + 1, numInputs + numY + 1):
                connections.append(ConnectGenes(x = i, Y = j, weight = random.randrange(-100, 100, 1), enabled = True))

        population.currentPop.append(Genome(connections = connections, nodes = nodes))


#lolwut?
def copy_to_popCap(gnome):
    for i in range(1, popCap):
        g = copy.deepcopy(gnome)
        for k in range(len(g.connections)):
            g.connections[k].weight = random.randrange(-100, 100, 1)
        population.currentPop.append(g)

#lolol alsowut?
def generate_connections(gnome):
    print('wut')

def run_game():
    for i in range(len(population.currentPop)):
        neuralNet = NeuralNet(population.currentPop[i])
        neuralNet.build_neural_net()
        population.currentPop[i].fitness = cartpole.get_fitness(neuralNet)
        # population.currentPop[i].mutate_weight()
        #population.mutate_weight(population.currentPop[i])
        # w = population.currentPop[i]

        # print(w.connections)


if '__main__' == __name__:
    popCap = 200
    numInputs, numY = cartpole.get_xy()
    numY = int(numY)
    i = 1
    while True:
        print("On generation ", i)
        start = clock()
        generate_initial_population()
        print("     generate_initial_population() time: ", clock() - start)
        run_game()
        start = clock()

        population.currentPop.sort(key = lambda x: x.fitness, reverse = True)
        print("     population.currentPop.sort() time: ", clock() - start)
        #to_json(population.currentPop[0])
        print("     Best fitness for this generation: ", population.currentPop[0].fitness)
        cartpole.render_game(population.currentPop[0])
        i += 1
