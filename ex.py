from ConnectGenes import ConnectGenes
from NodeGenes import NodeGenes
from Population import crossbreed

from BuildNeuralNet import NeuralNet
from Genome import Genome
import copy
import random
connections = []
nodes = []


nodes.append(NodeGenes(nodeNum = 1, t = 'Sensor'))
nodes.append(NodeGenes(nodeNum = 2, t = 'Sensor'))
nodes.append(NodeGenes(nodeNum = 3, t = 'Sensor'))
nodes.append(NodeGenes(nodeNum = 4, t = 'Hidden'))
nodes.append(NodeGenes(nodeNum = 5, t = 'Hidden'))
nodes.append(NodeGenes(nodeNum = 6, t = 'Output'))


connections.append(ConnectGenes(x = 1, Y = 4, weight = -10, enabled = True, innovation = 1))
connections.append(ConnectGenes(x = 1, Y = 6, weight = -30, enabled = True, innovation = 2))
connections.append(ConnectGenes(x = 1, Y = 5, weight = 30, enabled = True, innovation = 3))
connections.append(ConnectGenes(x = 2, Y = 4, weight = 20, enabled = True, innovation = 4))
#connections.append(ConnectGenes(x = 2, Y = 5, weight = -20, enabled = True, innovation = 5))
connections.append(ConnectGenes(x = 3, Y = 4, weight = 20, enabled = True, innovation = 6))
#connections.append(ConnectGenes(x = 3, Y = 5, weight = -20, enabled = True, innovation = 7))
connections.append(ConnectGenes(x = 4, Y = 6, weight = 20, enabled = True, innovation = 8))
connections.append(ConnectGenes(x = 5, Y = 6, weight = 20, enabled = True, innovation = 9))

connection = []
node = []

#connection.append(ConnectGenes(x = 1, Y = 4, weight = -15, enabled = True, innovation = 1))
#connection.append(ConnectGenes(x = 1, Y = 6, weight = -35, enabled = True, innovation = 2))
connection.append(ConnectGenes(x = 1, Y = 5, weight = 35, enabled = True, innovation = 3))
#connection.append(ConnectGenes(x = 2, Y = 4, weight = 25, enabled = True, innovation = 4))
connection.append(ConnectGenes(x = 2, Y = 5, weight = -25, enabled = True, innovation = 5))
#connection.append(ConnectGenes(x = 3, Y = 4, weight = 25, enabled = True, innovation = 6))
connection.append(ConnectGenes(x = 3, Y = 5, weight = -25, enabled = True, innovation = 7))
#connection.append(ConnectGenes(x = 5, Y = 6, weight = 25, enabled = True, innovation = 9))
connection.append(ConnectGenes(x = 5, Y = 7, weight = 22, enabled = True, innovation = 10))
connection.append(ConnectGenes(x = 7, Y = 6, weight = 22, enabled = True, innovation = 11))

node.append(NodeGenes(nodeNum = 1, t = 'Sensor'))
node.append(NodeGenes(nodeNum = 2, t = 'Sensor'))
node.append(NodeGenes(nodeNum = 3, t = 'Sensor'))
#node.append(NodeGenes(nodeNum = 4, t = 'Hidden'))
node.append(NodeGenes(nodeNum = 5, t = 'Hidden'))
node.append(NodeGenes(nodeNum = 7, t = 'Hidden'))
node.append(NodeGenes(nodeNum = 6, t = 'Output'))

crossbreed( Genome(connections = connection, nodes = node), Genome(connections = connections, nodes = nodes))
#connections.remove(y)
#print(Genome(connections = connections, nodes = nodes))
