#!/usr/bin/python3

"""Module to test max_integer_test function
"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test test the max_integer integer function
    """
    def test_6_max_integer_doc(self):
        """Tests the module documentation
        """
        m_doc = __import__("6-max_integer").__doc__
        self.assertTrue(len(m_doc) > 1)

    def test_6_max_integer_doc(self):
        """Tests the documentation of the function
        """
        f_doc = __import__("6-max_integer").max_integer.__doc__
        self.assertTrue(len(f_doc) > 1)

    def test_MaxInteger_positive(self):
        """Tests the function with a list of positive integers
        """
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(lst), max(lst))

    def test_MaxInteger_Negative(self):
        """Tests the function with a list of negative integers
        """
        lst = [-1, -98, -50, -4]
        self.assertEqual(max_integer(lst), max(lst))

    def test_MaxInteger_Floats(self):
        """Tests with a list of floats
        """
        lst = [4.5, 6.9, 98.9, 3.3, 0.6, 7.7, 9.10]
        self.assertEqual(max_integer(lst), max(lst))

    def test_MaxInteger_Beg(self):
        """Tests the function with a list of integers with the
            max integer at the begining of the list
        """
        lst = [45, 4, 5, 6, 7, 8, 9, 4, 7]
        self.assertEqual(max_integer(lst), max(lst))

    def test_MaxInteger_Mid(self):
        """Tests the function with a list of integers with the
            max integer at the begining of the list
        """
        lst = [4, 5, 6, 7, 90, 8, 9, 4, 7]
        self.assertEqual(max_integer(lst), max(lst))

    def test_MaxInteger_End(self):
        """Tests the function with a list of integers with the
            max integer at the begining of the list
        """
        lst = [4, 5, 6, 7, 90, 8, 9, 4, 7, 450]
        self.assertEqual(max_integer(lst), max(lst))

    def test_MaxInteger_Empty(self):
        """Tests the function with an empty list
        """
        lst = []
        self.assertIsNone(max_integer(lst))

    def test_MaxInteger_one(self):
        """Tests the function with one argument
        """
        lst = [1]
        self.assertEqual(max_integer(lst), 1)

    def test_MaxInteger_Zero(self):
        """Tests the function with a zero argument
        """
        self.assertIsNone(max_integer())
