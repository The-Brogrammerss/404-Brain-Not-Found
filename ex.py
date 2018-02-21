from NodeGenes import NodeGenes
from ConnectGenes import ConnectGenes
from Genome import Genome
from BuildNeuralNet import NeuralNet
import time


connections = []
nodes = []

nodes.append(NodeGenes(nodeNum = 1, t = 'Sensor'))
nodes.append(NodeGenes(nodeNum = 2, t = 'Sensor'))
nodes.append(NodeGenes(nodeNum = 3, t = 'Hidden'))
nodes.append(NodeGenes(nodeNum = 4, t = 'Hidden'))
nodes.append(NodeGenes(nodeNum = 5, t = 'Hidden'))
nodes.append(NodeGenes(nodeNum = 6, t = 'Output'))
nodes.append(NodeGenes(nodeNum = 7, t = 'Hidden'))
nodes.append(NodeGenes(nodeNum = 8, t = 'Output'))


connections.append(ConnectGenes(x = 1, Y = 4, weight = .1, enabled = True))
connections.append(ConnectGenes(x = 1, Y = 3, weight = .3, enabled = True))
connections.append(ConnectGenes(x = 2, Y = 3, weight = .7, enabled = True))
connections.append(ConnectGenes(x = 4, Y = 5, weight = .6, enabled = True))
connections.append(ConnectGenes(x = 3, Y = 5, weight = .4, enabled = True))
connections.append(ConnectGenes(x = 3, Y = 6, weight = .3, enabled = True))
connections.append(ConnectGenes(x = 5, Y = 6, weight = .2, enabled = True))
connections.append(ConnectGenes(x = 5, Y = 7, weight = .9, enabled = True))
connections.append(ConnectGenes(x = 7, Y = 8, weight = .9, enabled = True))

g = Genome()
g.connections = connections
g.nodes = nodes

nn = NeuralNet(g)

nn.buildNeuralNet()

for key, value in nn.inputLayer.items():
    print(str(key) +': '+ str(value))

for key, value in nn.hiddenLayers.items():
    print(str(key) +': '+ str(value))

for key, value in nn.outputLayer.items():
    print(str(key) +': '+ str(value))
start_time = time.time()
for i in range(100000):
    nn.predict([1,1])
print('Time: ' + str(time.time() - start_time))

print(nn.hiddenLayers[5])
print(nn.hiddenLayers[4])
print(nn.outputLayer[8])

'''
for key, value in nn.hiddenLayers[-2].items():
    print(str(key) +': '+ str(value))
'''
