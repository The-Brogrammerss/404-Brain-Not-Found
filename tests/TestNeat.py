import unittest
import NEAT
from Genome import Genome

class test_neat(unittest.TestCase):
    NEAT.numInputs = 2
    NEAT.numY = 1
    NEAT.popCap = 2
    NEAT.pop = []
    genPop = NEAT.GenerateInitPop()

    def test_generate_population(self):
        self.assertEqual(len(NEAT.pop), 2)