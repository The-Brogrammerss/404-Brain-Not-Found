from src.ConnectGenes import ConnectGenes
from src.NodeGenes import NodeGenes

from BuildNeuralNet import NeuralNet
from Genome import Genome
connections = []
nodes = []

nodes.append(NodeGenes(nodeNum = 1, t = 'Sensor'))
nodes.append(NodeGenes(nodeNum = 2, t = 'Sensor'))
nodes.append(NodeGenes(nodeNum = 3, t = 'Sensor'))
nodes.append(NodeGenes(nodeNum = 4, t = 'Hidden'))
nodes.append(NodeGenes(nodeNum = 5, t = 'Hidden'))
nodes.append(NodeGenes(nodeNum = 6, t = 'Output'))


connections.append(ConnectGenes(x = 1, Y = 4, weight = -10, enabled = True))
connections.append(ConnectGenes(x = 1, Y = 6, weight = -30, enabled = True))
connections.append(ConnectGenes(x = 1, Y = 5, weight = 30, enabled = True))
connections.append(ConnectGenes(x = 2, Y = 4, weight = 20, enabled = True))
connections.append(ConnectGenes(x = 2, Y = 5, weight = -20, enabled = True))
connections.append(ConnectGenes(x = 3, Y = 4, weight = 20, enabled = True))
connections.append(ConnectGenes(x = 3, Y = 5, weight = -20, enabled = True))
connections.append(ConnectGenes(x = 4, Y = 6, weight = 20, enabled = True))
connections.append(ConnectGenes(x = 5, Y = 6, weight = 20, enabled = True))


g = Genome()
g.connections = connections
g.nodes = nodes

nn = NeuralNet(g)

nn.build_neural_net()

for key, value in nn.inputLayer.items():
    print(str(key) +': '+ str(value))

for key, value in nn.hiddenLayers.items():
    print(str(key) +': '+ str(value))

for key, value in nn.outputLayer.items():
    print(str(key) +': '+ str(value))
nn.predict([1,0,0])
print("0 0 ", nn.output)
nn.predict([1,1,1])
print("1 1 ", nn.output)
nn.predict([1,0,1])
print("0 1 ", nn.output)
nn.predict([1,1,0])
print("1 0 ", nn.output)
