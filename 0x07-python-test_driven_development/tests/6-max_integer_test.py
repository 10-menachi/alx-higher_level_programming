#!/usr/bin/python3

"""
This module contains tests for the function max_integer
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTestCase(unittest.TestCase):
    """
    This class contains tests for the function max_integer
    """

    def test_empty_list(self):
        """
        Test that max_integer returns None for an empty list
        """
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """
        Test that max_integer returns the correct value for a single element list
        """
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """
        Test that max_integer returns the correct value for a list of positive numbers
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([10, 20, 30, 40, 50]), 50)

    def test_negative_numbers(self):
        """
        Test that max_integer returns the correct value for a list of negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-10, -20, -30, -40, -50]), -10)

    def test_mixed_numbers(self):
        """
        Test that max_integer returns the correct value for a list of mixed numbers
        """
        self.assertEqual(max_integer([-5, 0, 5]), 5)
        self.assertEqual(max_integer([-10, 0, 10]), 10)

    def test_duplicate_numbers(self):
        """
        Test that max_integer returns the correct value for a list of duplicate numbers
        """
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([10, 10, 10, 10]), 10)

    def test_mixed_list(self):
        """
        Test that max_integer returns the correct value for a list of mixed numbers
        """
        self.assertEqual(max_integer([1, -2, 3, -4, 5]), 5)
        self.assertEqual(max_integer([-10, 0, -30, 40, -50]), 40)


if __name__ == '__main__':
    unittest.main()
