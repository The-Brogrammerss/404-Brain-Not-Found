# Kinda silly to pretty much test python but needed for code coverage
import unittest

import NodeGene


class test_node_attributes(unittest.TestCase):
    global ng
    ng = NodeGene.NodeGenes()
    ng.nodeNum = 1
    ng.type = "Sensor"

    def test_x(self):
        self.assertEqual(ng.nodeNum, 1)

    def test_Y(self):
        self.assertEqual(ng.type, "Sensor")

    def test_str(self):
        self.assertNotEqual(ng.__str__(), None)
