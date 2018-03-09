# This is where most if not all of the GA and NEAT logic will happen.
import copy
import random
from src import cartpole
from src.misc.Json import to_json
from src.BuildNeuralNet import NeuralNet
from src.ConnectGenes import ConnectGenes
from src.Genome import Genome
from src.NodeGenes import NodeGenes

innovation = 0


def generate_initial_genome():
    gnome = Genome()
    #for i in range(1, numInputs + 2):
    for i in range(1, numInputs + 1):
        nodes = NodeGenes()
        nodes.nodeNum = i
        nodes.type = "Sensor"
        gnome.nodes.append(nodes)

    for i in range(1, numY + 1):
        nodes = NodeGenes()
        nodes.nodeNum = numInputs + i
        nodes.type = "Output"
        gnome.nodes.append(nodes)

    generate_connections(gnome)
    population.append(gnome)
    copy_to_popCap(gnome)


def copy_to_popCap(gnome):
    for i in range(1, popCap):
        g = copy.deepcopy(gnome)
        for k in range(len(g.connections)):
            g.connections[k].weight = random.randrange(-100, 100, 1)
        population.append(g)


def generate_connections(gnome):
    global innovation
    for k in range(0, len(gnome.nodes)):
        if gnome.nodes[k].type == "Sensor":
            for j in range(1, len(gnome.nodes)):
                if gnome.nodes[j].type == "Output":
                    cons = ConnectGenes()
                    cons.x = gnome.nodes[k].nodeNum
                    cons.Y = gnome.nodes[j].nodeNum
                    cons.enabled = True
                    innovation = innovation + 1
                    cons.innovation = innovation
                    cons.weight = random.randint(-10, 10)
                    gnome.connections.append(cons)


def run_game():
    for i in range(len(population)):
        neuralNet = NeuralNet(population[i])
        neuralNet.build_neural_net()
        population[i].fitness = cartpole.get_fitness(neuralNet)

if '__main__' == __name__:
    popCap = 200


    population = []
    # os.system("cartpole.py")
    numInputs, numY = cartpole.get_xy()

    numY = int(numY)
    generate_initial_genome()

    run_game()
    population.sort(key = lambda x: x.fitness, reverse = True)

    to_json(population[0])
    cartpole.render_game(population[0])
    # cartpole.render_game(misc.Json.from_jason())