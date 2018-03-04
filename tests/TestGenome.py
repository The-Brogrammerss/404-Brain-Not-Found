# Kinda silly to pretty much test python but needed for code coverage
import unittest

from src.Genome import Genome

from src.ConnectGenes import ConnectGenes
from src.NodeGenes import NodeGenes


class test_genome(unittest.TestCase):
    global g
    g = Genome()
    g.connections.append(ConnectGenes())
    g.nodes.append(NodeGenes())

    g.nodes[0].nodeNum = 4
    g.nodes[0].type = "Sensor"
    def test_nodeNum(self):
        self.assertEqual(g.nodes[0].nodeNum, 4)

    def test_type(self):
        self.assertEqual(g.nodes[0].type, "Sensor")

    def test_str(self):
        self.assertNotEqual(g.__str__(), None)

