#!/usr/bin/python3

"""module to implement the class Square
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class Square
    """

    def __init__(self, size):
        """initialises the class
        Args:
            size (int): size of Square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        A function that calculates the area of the Square
        """
        return self.__size ** 2
