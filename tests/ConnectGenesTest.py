import unittest

class test_Connect(unittest.TestCase):
    # Added these test to test making lower case
    global pr
    pr = palindrome_recursive()

    def test_none(self):
        self.assertEquals (pr.to_lowercase(None), None)
    def test_one_lower(self):
        self.assertEquals (pr.to_lowercase("a"), "a")
    def test_one_upper(self):
        self.assertEquals (pr.to_lowercase("B"), "b")
    def test_multiple_lower(self):
        self.assertEquals (pr.to_lowercase("abcdz"), "abcdz")
    def test_mix(self):
        self.assertEquals (pr.to_lowercase("Hip Replacement"), "hip replacement")