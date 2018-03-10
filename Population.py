import random
import copy
from Genome import Genome

class Population(object):

    def __init__(self, pop):
        self.currentPop = pop
        self.innovationCounter = 0
        self.connectionList = []
        self.maxNodes = 0


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
