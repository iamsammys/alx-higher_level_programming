#!/usr/bin/python3

"""A module to implement the addition of two numbers
"""


def add_integer(a, b=98):
    """A function to calculate the addition of two numbers

    Returns:
        int: the sum of the args
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
