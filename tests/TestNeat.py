import unittest
import NEAT

class test_neat(unittest.TestCase):
    NEAT.numInputs = 2
    NEAT.numY = 1
    NEAT.popCap = 2
    NEAT.pop = []
    genPop = NEAT.GenerateInitialPopulation()

    def test_generate_population(self):
        self.assertEqual(len(NEAT.pop), 2)

    def test_generated_connections_x(self):
        self.assertEqual(NEAT.pop[0].connections[0].x, 1)

    def test_generated_connections_Y(self):
        self.assertEqual(NEAT.pop[0].connections[0].Y, 4)

    def test_generated_connections_enabled(self):
        self.assertEqual(NEAT.pop[0].connections[1].enabled, True)

    def test_generated_connections_weight(self):
        self.assertNotEqual(NEAT.pop[0].connections[0].weight, None)

    def test_generated_connections_inovation_num(self):
        self.assertEqual(NEAT.pop[0].connections[2].innovation, 3)
