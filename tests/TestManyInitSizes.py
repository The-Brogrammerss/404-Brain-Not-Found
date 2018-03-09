import unittest

import NEAT


class test_many_sizes(unittest.TestCase):
    for i in range(1, 20):
        NEAT.numInputs = i
        for k in range(1, 20):
            NEAT.numY = k

