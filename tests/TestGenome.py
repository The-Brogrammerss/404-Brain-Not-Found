import unittest
import copy
import NEAT

from Genome import Genome
from ConnectGene import ConnectGene
from NodeGene import NodeGene
from Population import Population


class test_genome(unittest.TestCase):
    global g
    g = Genome()
    g.connections.append(ConnectGene())
    g.nodes.append(NodeGene())
    g.nodes[0].nodeNum = 4
    g.nodes[0].type = "Sensor"

    def setUp(self):
        NEAT.numInputs = 2
        NEAT.numY = 1
        NEAT.popCap = 2
        NEAT.population = Population()
        NEAT.generate_initial_population()

    def test_nodeNum(self):
        self.assertEqual(g.nodes[0].nodeNum, 4)

    def test_type(self):
        self.assertEqual(g.nodes[0].type, "Sensor")

    def test_str(self):
        self.assertNotEqual(g.__str__(), None)

    def test_mutate_weight(self):
        new_genome = copy.deepcopy(NEAT.population.currentPop[0])
        NEAT.population.mutate_weight(new_genome)
        self.assertNotEqual(NEAT.population.currentPop[1], g, True)

