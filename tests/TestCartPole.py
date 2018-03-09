import unittest

import cartpole


class test_cartPole(unittest.TestCase):
    def test_getxY(self):
        self.assertEqual(cartpole.get_xy(), (5, 1))