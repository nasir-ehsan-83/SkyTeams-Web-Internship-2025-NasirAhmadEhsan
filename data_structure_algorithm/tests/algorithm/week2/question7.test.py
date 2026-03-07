import unittest
from algorithm.week2.question7 import is_even

class TestQuestion7(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))
        self.assertTrue(is_even(0))

if __name__ == "__main__":
    unittest.main()
