#!/usr/bin/python3
"""Module that defines the class Square
"""


class Square:
    """A class Square
    """
    def __init__(self, size=0):
        """Initialises the objects of the class

        Args:
            size (int): The size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the Square

        Return:
            int: The size of the Square
        """
        return self.__size ** 2
