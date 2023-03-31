#!/usr/bin/python3

"""Module for printing a fullname
"""


def say_my_name(first_name, last_name=""):
    """Prints the first and last names

    Args:
        first_name (str): The first name to be printed
        last_name (str): The last name to be printed
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
