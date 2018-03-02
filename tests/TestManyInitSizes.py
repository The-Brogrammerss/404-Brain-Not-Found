import unittest
from Genome import Genome
from ConnectGenes import ConnectGenes
from NodeGenes import NodeGenes
import NEAT

class test_many_sizes(unittest.TestCase):
    for i in range(1, 20):
        NEAT.numInputs = i
        for k in range(1, 20):
            NEAT.numY = k

