import unittest

from src import NEAT


class TestNeat(unittest.TestCase):

    NEAT.numInputs = 10
    NEAT.numY = 10
    NEAT.popCap = 2
    NEAT.population = []
    genPop = NEAT.generate_initial_genome()

    def test_generate_population(self):
        self.assertEqual(len(NEAT.population), 2)

    def test_generated_connections_x(self):
        self.assertEqual(NEAT.population[0].connections[0].x, 3)

    def test_generated_connections_Y(self):
        self.assertEqual(NEAT.population[0].connections[0].Y, 1)

    def test_generated_connections_enabled(self):
        self.assertEqual(NEAT.population[0].connections[1].enabled, True)

    def test_generated_connections_weight(self):
        self.assertNotEqual(NEAT.population[0].connections[0].weight, None)

    def test_generated_connections_inovation_num(self):
        self.assertEqual(NEAT.population[0].connections[2].innovation, 3)
