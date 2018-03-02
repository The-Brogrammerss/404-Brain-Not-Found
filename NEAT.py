from ConnectGenes import ConnectGenes
from Genome import Genome
from NodeGenes import NodeGenes
import cartpole
from BuildNeuralNet import NeuralNet
import copy
import random
import cartpole
import gym

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
        neuralNet.buildNeuralNet()
        population[i].fitness = cartpole.get_fitness(neuralNet)

if '__main__' == __name__:
    popCap = 200
    population = []
    # os.system("cartpole.py")
    numInputs, numY = cartpole.get_xy()

    numY = int(numY)
    print("num ouputs:", numY)
    print("num Inputs:", numInputs)
    generate_initial_genome()

    nn = NeuralNet(genome = population[0])
    nn.buildNeuralNet()
    for key, value in nn.inputLayer.items():
        print(str(key) +': '+ str(value))
    for key, value in nn.outputLayer.items():
        print(str(key) +': '+ str(value))
    nn.predict([1,1,1,1,1])
    print(nn.output)

    run_game()
    population.sort(key = lambda x: x.fitness, reverse = True)
    print(population[0].fitness)
    env = gym.make('CartPole-v1')
    NN = NeuralNet(genome = population[0])
    NN.buildNeuralNet()

    observation = env.reset()
    observation = observation.tolist()
    observation.append(1)
    print("observation: " + str(observation))
    fitness = 0
    for x in range(10000):

        NN.predict(observation)
        observation, reward, done, info = env.step(round(NN.output[0]))
        env.render()
        observation = observation.tolist()
        observation.append(1)
        fitness += reward
        if done:
            break
