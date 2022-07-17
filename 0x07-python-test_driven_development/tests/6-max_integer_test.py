#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
import sys

# directory = """/home/estifanos/ALX_Repo/alx-higher_level_programming/0x07-
# python-test_driven_development"""
# sys.path.insert(0, directory)
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 4, -1]), 4)
        self.assertEqual(max_integer([-10, 0, 5]), 5)
        self.assertEqual(max_integer([4, 0, -1, 4, 2]), 4)
