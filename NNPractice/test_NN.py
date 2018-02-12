import unittest
import numpy.testing as npT
import NNPractice

npT.test('full')

class test_NN (unittest.TestCase):
    def test_sigmoid_0(self):
        self.assertEqual(NNPractice.Neural_Net.sigmoid(0), 0.5)

    def test_sigmoid_458(self):
        self.assertEqual(NNPractice.Neural_Net.sigmoid(0.458), 0.61253961344091512)

    def test_sigmoid_array(self):
        z = [0.2,  0.4,  0.1]
        npT.assert_allclose(NNPractice.Neural_Net.sigmoid(z), [0.549834, 0.59868766, 0.52497919])

