#!/usr/bin/python3

"""module to implement isinstace
"""


def is_same_class(obj, a_class):
    """checks whether an object is exactly an instance of a class
    """
    return (isinstance(obj, a_class) and type(obj) is a_class)
