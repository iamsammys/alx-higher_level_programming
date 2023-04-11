#!/usr/bin/python3

"""Implements a class my_list
"""


class MyList(list):
    """my_list class
    """
    def print_sorted(self):
        """prints the sorted form of the list
        """
        my_lst = sorted(self)
        print(my_lst)
