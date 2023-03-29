#!/usr/bin/python3

"""A module for the class square
"""


class Square:
    """Class square
    """
    def __init__(self, size=0):
        """Initialises the instances of the class Square

        Args:
            size (int): size of the Square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
