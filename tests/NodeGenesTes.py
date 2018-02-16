# Kinda redundant as in its testing python but oh well
import unittest
import NodeGenes

class test_Connect(unittest.TestCase):
    # Added these test to test making lower case
    global ng
    ng = NodeGenes.NodeGenes()
    ng.nodeNum = 1
    ng.type = "Sensor"

    def test_x(self):
        self.assertEqual(ng.nodeNum, 1)

    def test_Y(self):
        self.assertEqual(ng.type, "Sensor")
