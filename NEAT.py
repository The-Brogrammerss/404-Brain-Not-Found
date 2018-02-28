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

def GenerateInitialPopulation():
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

    GenerateConnections(gnome)

    pop.append(gnome)
    for i in range(1, popCap):
        g = copy.deepcopy(gnome)
        for k in range(len(g.connections)):
            g.connections[k].weight = random.randrange(-100, 100, 1)
        pop.append(g)


def GenerateConnections(gnome):
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


def RunGame():
    for i in range(len(pop)):
        neuralNet = NeuralNet(pop[i])
        #print(pop[i])
        neuralNet.buildNeuralNet()
        pop[i].fitness = cartpole.get_fitness(neuralNet)
        #print(pop[i].fitness)

if '__main__' == __name__:
    popCap = 200
    pop = []
    # os.system("cartpole.py")
    numInputs, numY = cartpole.get_xy()

    numY = int(numY)
    print("num ouputs:", numY)
    print("num Inputs:", numInputs)
    GenerateInitialPopulation()

    nn = NeuralNet(genome = pop[0])
    nn.buildNeuralNet()
    for key, value in nn.inputLayer.items():
        print(str(key) +': '+ str(value))
    for key, value in nn.outputLayer.items():
        print(str(key) +': '+ str(value))
    nn.predict([1,1,1,1,1])
    print(nn.output)

    RunGame()
    pop.sort(key = lambda x: x.fitness, reverse = True)
    print(pop[0].fitness)
    env = gym.make('CartPole-v1')
    NN = NeuralNet(genome = pop[0])
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
