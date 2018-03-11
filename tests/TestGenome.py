# Kinda silly to pretty much test python but needed for code coverage
import unittest
import copy
import NEAT

from Genome import Genome
from ConnectGenes import ConnectGenes
from NodeGenes import NodeGenes


class test_genome(unittest.TestCase):
    global g
    g = Genome()
    g.connections.append(ConnectGenes())
    g.nodes.append(NodeGenes())
    g.nodes[0].nodeNum = 4
    g.nodes[0].type = "Sensor"

    def setUp(self):
        NEAT.numInputs = 2
        NEAT.numY = 1
        NEAT.popCap = 2
        NEAT.population = []
        NEAT.generate_initial_genome()

    def test_nodeNum(self):
        self.assertEqual(g.nodes[0].nodeNum, 4)

    def test_type(self):
        self.assertEqual(g.nodes[0].type, "Sensor")

    def test_str(self):
        self.assertNotEqual(g.__str__(), None)

    def test_mutate_weight(self):
        print(NEAT.population[0].connections[0])
        new_genome = copy.deepcopy(NEAT.population[0])
        new_genome.mutate_weight()
        self.assertNotEqual(new_genome, g, True)

