#!/usr/bin/python3

"""Module to test max_integer_test function
"""

import unittest
max_int = __import__("6-max_integer").max_integer


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

