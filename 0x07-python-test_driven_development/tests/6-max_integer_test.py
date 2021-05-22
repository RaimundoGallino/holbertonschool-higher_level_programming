#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""

    def test_ispositive(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_isnegative(self):
        self.assertEqual(max_integer([-1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_single_element(self):
        self.assertEqual(max_integer([-4]), -4)
        self.assertEqual(max_integer([-3, 4]), 4)

    def test_floats(self):
        self.assertEqual(max_integer([0.2, 0.5], 0.5))
        self.assertEqual(max_integer([1.3, 0.4, 0.7, 9.0, 1.3]), 9.0)

if __name__ == '__main__':
    unittest.main()
