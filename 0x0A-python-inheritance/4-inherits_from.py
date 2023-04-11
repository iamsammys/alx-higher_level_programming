#!/usr/bin/python3

"""module to implement issubclass
"""


def inherits_from(obj, a_class):
    """check if the object is an instance of a class
    """
    return (issubclass(obj.__class__, a_class) and type(obj) is not a_class)
