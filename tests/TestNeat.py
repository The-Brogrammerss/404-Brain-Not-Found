import unittest

import NEAT
from Genome import Genome
from ConnectGene import ConnectGene
from Population import Population



class TestNeat(unittest.TestCase):
    def setUp(self):
        population = Population()
        NEAT.numInputs = 2
        NEAT.numY = 1
        NEAT.popCap = 2
        NEAT.population = []
        NEAT.generate_initial_population()
        con1 = ConnectGene(x=1, Y=3, enabled=True, weight=10, innovation=3)


