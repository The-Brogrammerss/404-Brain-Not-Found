import unittest

from src.Genome import Genome

from src.BuildNeuralNet import NeuralNet
from src.ConnectGenes import ConnectGenes
from src.NodeGenes import NodeGenes


class test_build_neural_net(unittest.TestCase):
    global nn
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

    genome = Genome(connections = connections, nodes = nodes)
    nn = NeuralNet(genome = genome)

    def test_buildNueralNet(self):
        nn.build_neural_net()
        self.assertEqual(nn.inputLayer[2].outgoing, [4, 5])
        self.assertEqual(nn.hiddenLayers[4].weights[2], 20)
        self.assertEqual(nn.outputLayer[6].type, 'Output')

    def test_predict(self):
        nn.predict([1,0,0])
        self.assertEqual(int(round(nn.output[0])), 0)
        nn.predict([1,1,1])
        self.assertEqual(int(round(nn.output[0])), 0)
        nn.predict([1,0,1])
        self.assertEqual(int(round(nn.output[0])), 1)
        nn.predict([1,1,0])
        self.assertEqual(int(round(nn.output[0])), 1)
