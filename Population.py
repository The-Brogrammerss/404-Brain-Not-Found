import random
import copy
from Genome import Genome
from ConnectGene import ConnectGenes
from Config import Config
from NodeGene import NodeGenes


class Population(object):

    def __init__(self):
        self.currentPop = []
        self.innovationCounter = 0
        self.connectionList = []
        self.pair = 1


    def mutate_weight(self, genome):
        perturb_rate = 0.9
        perturb_chance = random.random()
        random_connection = random.randint(0, len(genome.connections) - 1)
        if perturb_chance <= perturb_rate:
            genome.connections[random_connection].weight = round(
                genome.connections[random_connection].weight * random.uniform(0.8, 1.2))
            if genome.connections[random_connection].weight > 100:
                genome.connections[random_connection].weight = 100
            elif genome.connections[random_connection].weight < -100:
                genome.connections[random_connection].weight = -100
        else:
            genome.connections[random_connection].weight = random.randrange(-100, 100, 1)



    def mutate_add_connection(self, genome):
        available_connections = []

        for nodeX in genome.nodes:
            for nodeY in genome.nodes:
                if nodeY.layer > nodeX.layer and not any(con.x == nodeX.nodeNum and con.Y == nodeY.nodeNum for con in genome.connections):
                    available_connections.append([nodeX.nodeNum, nodeY.nodeNum])

        if len(available_connections) > 0:
            connection = available_connections[random.randint(0, len(available_connections) - 1)]
            master_connection = next((con for con in self.connectionList if con.x == connection[0] and con.Y == connection[1]), None)
            if master_connection != None:
                genome.connections.append(ConnectGenes(x = connection[0], Y = connection[1], weight = random.randrange(-100, 100, 1), enabled = True, innovation = master_connection.innovation))
            else:
                self.innovationCounter += 1
                self.connectionList.append(ConnectGenes(x = connection[0], Y = connection[1], innovation = self.innovationCounter))
                genome.connections.append(ConnectGenes(x = connection[0], Y = connection[1], innovation = self.innovationCounter, weight = random.randrange(-100, 100, 1), enabled = True))

    def mutate_add_node(self, genome):
        '''
        Grab genome from pop

        pick random connection

        check master connection list
            grab all connections with correct x
        generate new connection
        '''
        # genome = self.currentPop[index]

        connection = genome.connections[random.randint(0, len(genome.connections) - 1)]

        startingNodesToCheck = [conGene for conGene in self.connectionList if conGene.x == connection.x]
        nodesToCheck = [conGene.Y for conGene in startingNodesToCheck]
        back_half = [conGene for conGene in self.connectionList if conGene.x in nodesToCheck and conGene.Y == connection.Y]
        connection.enabled = False

        if len(back_half) == 1:
            front_half = [conGene for conGene in startingNodesToCheck if conGene.Y == back_half[0].x][0]

            node = [nodeGene for nodeGene in genome.nodes if nodeGene.nodeNum == front_half.x][0]
            layer = 1 if node.layer == float('-inf') else node.layer + 1

            genome.connections.append(ConnectGenes(x = front_half.x, Y = front_half.Y, innovation = front_half.innovation,
                                        weight = 100, enabled = True ))
            genome.connections.append(ConnectGenes(x = back_half[0].x, Y = back_half[0].Y, innovation = back_half[0].innovation,
                                        weight = connection.weight, enabled = True))
            genome.nodes.append(NodeGenes(nodeNum = front_half.Y, t = "Hidden", layer = layer))

            #return genome
        else:
            self.maxNodes += 1
            self.innovationCounter += 1

            node = [nodeGene for nodeGene in genome.nodes if nodeGene.nodeNum == connection.x][0]
            layer = 1 if node.layer == float('-inf') else node.layer + 1

            genome.nodes.append(NodeGenes(nodeNum = self.maxNodes, t = "Hidden", layer = layer))
            genome.connections.append(ConnectGenes(x = connection.x, Y = self.maxNodes, weight = 100,
                                        innovation = self.innovationCounter, enabled = True, pair = self.pair))
            self.connectionList.append(ConnectGenes(x = connection.x, Y = self.maxNodes, innovation = self.innovationCounter))

            self.innovationCounter += 1
            genome.connections.append(ConnectGenes(x = self.maxNodes, Y = connection.Y, weight = connection.weight,
                                        innovation = self.innovationCounter, enabled = True, pair = self.pair))
            self.connectionList.append(ConnectGenes(x = self.maxNodes, Y = connection.Y, innovation = self.innovationCounter))
            self.pair += 1
            #return genome


def crossbreed(genome_one, genome_two):
    # TODO There was a 75% chance that an inherited gene was disabled if it was disabled in either parent.
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
