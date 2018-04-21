import unittest

import NEAT
from Genome import Genome
from ConnectGene import ConnectGene
from Population import Population



class TestNeat(unittest.TestCase):
    def setUp(self):
        NEAT.numInputs = 2
        NEAT.numY = 1
        NEAT.popCap = 5
        # NEAT.generate_initial_population()
        NEAT.population = Population()
        con1 = ConnectGene(x=1, Y=3, enabled=True, weight=70, innovation=3)
        con2 = ConnectGene(weight=-80, innovation=1)
        genome1 = Genome()
        genome2 = Genome()
        genome1.connections.append(con1)
        genome2.connections.append(con2)
        NEAT.population.currentPop.append([genome1])
        NEAT.population.currentPop.append([genome2])

        NEAT.next_gen = Population()
        con1 = ConnectGene(x=1, Y=3, enabled=True, weight=20, innovation=3)
        con2 = ConnectGene(weight=40, innovation=2)
        genome3 = Genome()
        genome4 = Genome()
        genome3.connections.append(con1)
        genome4.connections.append(con2)
        NEAT.next_gen.currentPop.append(genome3)
        NEAT.next_gen.currentPop.append(genome4)


    def test_speciate(self):
        # self.assertEqual(NEAT.speciate(),)
        NEAT.speciate()
        # NEAT.next_gen.currentPop[1].append(Genome())
        # print("next_gen pop len", len(NEAT.next_gen.currentPop))
        print("next_gen pop:", NEAT.next_gen.currentPop)