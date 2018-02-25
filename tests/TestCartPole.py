import unittest
from cartpole import CartPole
class test_cartPole(unittest.TestCase):
    def test_getxY(self):
        self.assertEqual(CartPole.getXy(self), (4, 2))