from ConnectGenes import ConnectGenes
from Genome import Genome
from NodeGenes import NodeGenes
from cartpole import CartPole
import copy
import random
import cartpole

innovation = 0

def GenerateInitPop():
    gnome = Genome()

    for i in range(1, numInputs + 2):
        nodes = NodeGenes()
        nodes.nodeNum = i
        nodes.type = "Sensor"
        gnome.nodes.append(nodes)

    for i in range(1, numY + 1):
        nodes = NodeGenes()
        nodes.nodeNum = numInputs + i + 1
        nodes.type = "Output"
        gnome.nodes.append(nodes)

    GenerateConnections(gnome)

    pop.append(gnome)
    for i in range(1, popCap):
        g = copy.deepcopy(gnome)
        for k in range(len(g.connections)):
            g.connections[k].weight = random.random()
        pop.append(g)
    print(pop[0])
    print(pop[199])

def GenerateConnections(gnome):
    global innovation
    for k in range(0, len(gnome.nodes)):
        if gnome.nodes[k].type == "Sensor":
            for j in range(1, len(gnome.nodes)):
                if gnome.nodes[j].type == "Output":
                    cons = ConnectGenes()
                    cons.x = gnome.nodes[k].nodeNum
                    cons.Y = gnome.nodes[j].nodeNum
                    innovation = innovation + 1
                    cons.innovation = (innovation)
                    cons.weight = random.random()
                    gnome.connections.append(cons)




if '__main__' == __name__:
    popCap = 200
    pop = []
    # os.system("cartpole.py")
    numInputs, numY = CartPole.getXy()
    numY = int(numY)
    print("num ouputs:", numY)
    print("num Inputs:", numInputs)
    GenerateInitPop()