import random
import copy
from Genome import Genome
from ConnectGenes import ConnectGenes
from Config import Config
from NodeGenes import NodeGenes


class Population(object):

    def __init__(self, pop):
        self.currentPop = pop
        self.innovationCounter = 0
        self.connectionList = []
        self.maxNodes = 0

    def mutate_weight(self, index):
        genome = self.currentPop[index]
        perturb_rate = 0.9
        perturb_chance = random.random()
        random_connection = random.randint(0, len(genome.connections) - 1)
        if perturb_chance <= perturb_rate:
            genome.connections[random_connection].weight = round(
                genome.connections[random_connection].weight * random.uniform(0.8, 1.2))

        else:
            genome.connections[random_connection].weight = random.randrange(-100, 100, 1)
        self.currentPop[index] = genome

    def mutate_add_node(self, index):
        print("Before______________________", len(self.connectionList))
        for con in range(len(self.currentPop[index].connections)):
            print(self.currentPop[index].connections[con])
        genome = self.currentPop[index]
        front_half = ConnectGenes()
        back_half = ConnectGenes()
        new_node = NodeGenes()
        random_connection = random.randint(0, len(genome.connections) - 1)
        Y = genome.connections[random_connection].Y
        x = genome.connections[random_connection].x
        # self.maxNodes = self.maxNodes + 1
        # new_node_num = self.maxNodes
        new_node_num = len(self.currentPop[index].nodes) + 1
        new_node.nodeNum = new_node_num
        new_node.type = "Hidden"
        genome.nodes.append(new_node)

        front_half.x = x
        front_half.Y = new_node_num
        front_half.enabled = True
        front_half.weight = Config.dict["max_weight"]

        back_half.x = new_node_num
        back_half.Y = Y
        back_half.enabled = True
        back_half.weight = random.randrange(Config.dict["min_weight"],
                                            Config.dict["max_weight"],
                                            Config.dict["weight_step"])
        cl = self.connectionList
        for gene in range (len(self.connectionList)):
            if cl[gene].x == front_half.x:
                for gene2 in range (len(self.connectionList)):
                    if cl[gene].Y == cl[gene2].x and cl[gene2].Y == Y:
                        front_half.innovation = cl[gene].innovation
                        back_half.innovation = cl[gene2].innovation
                        genome.connections.append(front_half)
                        genome.connections.append(back_half)
                        # self.connectionList.append(front_half)
                        # self.connectionList.append(back_half)
                        break

                    elif cl[gene].Y == Y:
                        # genome.connections[random_connection].enabled = False
                        genome.connections[random_connection].enabled = False
                        self.innovationCounter = self.innovationCounter + 1
                        front_half.innovation = self.innovationCounter
                        genome.connections.append(front_half)
                        self.connectionList.append(front_half)

                        self.innovationCounter = self.innovationCounter + 1
                        back_half.innovation = self.innovationCounter
                        genome.connections.append(back_half)
                        self.connectionList.append(back_half)
                        break


        print("After__________________________", len(self.connectionList))
        for con in range(len(self.currentPop[index].connections)):
            print(self.currentPop[index].connections[con])
        self.currentPop[index] = genome


def crossbreed(genome_one, genome_two):
    child_connections = []
    child_nodes = []

    g1 = copy.deepcopy(genome_one.connections)
    g2 = copy.deepcopy(genome_two.connections)

    for i, gene1 in enumerate(g1):
        gene2 = next((x for x in g2 if x.innovation == gene1.innovation), None)
        if gene2 != None:
            if random.randint(0,1):
                child_connections.append(gene1)
            else:
                child_connections.append(gene2)
                if not any(x.nodeNum == gene2.x for x in child_nodes):
                    child_nodes.append(next(x for x in genome_two.nodes if x.nodeNum == gene2.x))
                if not any(x.nodeNum == gene2.Y for x in child_nodes):
                    child_nodes.append(next(x for x in genome_two.nodes if x.nodeNum == gene2.Y))
            #This might cause issues later
            g2.remove(gene2)
        else:
            child_connections.append(gene1)
        if not any(x.nodeNum == gene1.x for x in child_nodes):
            child_nodes.append(next(x for x in genome_one.nodes if x.nodeNum == gene1.x))
        if not any(x.nodeNum == gene1.Y for x in child_nodes):
            child_nodes.append(next(x for x in genome_one.nodes if x.nodeNum == gene1.Y))

    for gene in g2:
        child_connections.append(gene)
        if not any(x.nodeNum == gene.x for x in child_nodes):
            child_nodes.append(next(x for x in genome_two.nodes if x.nodeNum == gene.x))
        if not any(x.nodeNum == gene.Y for x in child_nodes):
            child_nodes.append(next(x for x in genome_two.nodes if x.nodeNum == gene.Y))

    child_connections.sort(key=lambda x: x.innovation)
    child_nodes.sort(key=lambda x: x.nodeNum)

    return Genome(connections = child_connections, nodes = child_nodes)
