# Kinda redundant as in its testing python but oh well
import unittest
import ConnectGenes

class test_Connect(unittest.TestCase):
    # Added these test to test making lower case
    global cg
    cg = ConnectGenes.ConnectGenes()
    cg.x = 1
    cg.Y = 2
    cg.weight = 0.7
    cg.enabled = True
    cg.innovation = 1

    def test_x(self):
        self.assertEqual(cg.x, 1)

    def test_Y(self):
        self.assertEqual(cg.Y, 2)

    def test_weight(self):
        self.assertEqual(cg.weight, 0.7)

    def test_enabled(self):
        self.assertEqual(cg.enabled, True)

    def test_innovation(self):
        self.assertEqual(cg.innovation, 1)

