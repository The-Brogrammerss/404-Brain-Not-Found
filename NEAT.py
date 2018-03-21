# This is where most if not all of the GA and NEAT logic will happen.
import copy
import random

from ConnectGenes import ConnectGenes
from Genome import Genome
from NodeGenes import NodeGenes
from Population import Population
from Config import Config
from BuildNeuralNet import NeuralNet
from Population import crossbreed

import cartpole
from misc.Json import to_json


def generate_initial_genome():
    gnome = Genome()
    for i in range(1, numInputs + 1):
        nodes = NodeGenes()
        nodes.nodeNum = i
        population.maxNodes = population.maxNodes + i
        nodes.type = "Sensor"
        gnome.nodes.append(nodes)

    for i in range(1, numY + 1):
        nodes = NodeGenes()
        nodes.nodeNum = numInputs + i
        population.maxNodes = numInputs + i
        nodes.type = "Output"
        gnome.nodes.append(nodes)

    generate_connections(gnome)
    population.currentPop.append(gnome)
    copy_to_popCap(gnome)


def copy_to_popCap(gnome):
    for i in range(1, popCap):
        g = copy.deepcopy(gnome)
        for k in range(len(g.connections)):
            g.connections[k].weight = random.randrange(-100, 100, 1)
        population.currentPop.append(g)


def generate_connections(gnome):
    for k in range(0, len(gnome.nodes)):
        if gnome.nodes[k].type == "Sensor":
            for j in range(1, len(gnome.nodes)):
                if gnome.nodes[j].type == "Output":
                    cons = ConnectGenes()
                    cons.x = gnome.nodes[k].nodeNum
                    cons.Y = gnome.nodes[j].nodeNum
                    cons.enabled = True
                    population.innovationCounter = population.innovationCounter + 1
                    cons.innovation = population.innovationCounter
                    cons.weight = random.randrange(Config.dict["min_weight"],
                                                   100, 1)
                    gnome.connections.append(cons)
                    population.connectionList.append(cons)


def git_gud():
    for gnome in range(int(round(.1 * popCap))):
        next_gen.currentPop.append(copy.deepcopy(population.currentPop[gnome]))
    for gnome in range(int(round(.9 * popCap))):
        next_gen.currentPop.append(crossbreed(population.currentPop[gnome],
                                              random.choice(population.currentPop[:popCap])))
    for gnome in range(int(round(.4 * popCap))):
        next_gen.mutate_weight(gnome)

    for gnome in range(int(round(.01 * popCap))):
        next_gen.mutate_add_node(random.randint(0, popCap))
    # next_gen.mutate_add_node(random.choice(population.currentPop[:popCap]))


def run_game():
    for i in range(len(population.currentPop)):
        neuralNet = NeuralNet(population.currentPop[i])
        neuralNet.build_neural_net()
        population.currentPop[i].fitness = cartpole.get_fitness(neuralNet)
        # population.currentPop[i].mutate_weight()
        # population.mutate_weight(population.currentPop[i])
        # w = population.currentPop[i]

        # print(w.connections)


if '__main__' == __name__:
    popCap = 100
    population = Population([])
    next_gen = Population([])
    numInputs, numY = cartpole.get_xy()
    numY = int(numY)
    generate_initial_genome()
    # while True:
    for i in range(3):

        run_game()
        population.currentPop.sort(key = lambda x: x.fitness, reverse = True)
        # cartpole.render_game(population.currentPop[0])
        next_gen.maxNodes = population.maxNodes
        next_gen.innovationCounter = population.innovationCounter
        next_gen.connectionList = population.connectionList
        git_gud()
        population = next_gen
        to_json(population.currentPop[0])
    print("_____________________Connection list___________________")
    for con in range (len(next_gen.connectionList)):
        print(next_gen.connectionList[con])
