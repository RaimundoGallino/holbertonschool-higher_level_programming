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

if __name__ == '__main__':
    unittest.main()
