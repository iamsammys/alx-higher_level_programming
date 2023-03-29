#!/usr/bin/python3

"""A module for Square class
"""


class Square:
    """A class Square
    """
    def __init__(self, size=0):
        """Initialises the objects of the class
        
        Args:
            size (int): The size of the Square
        """
        self.size = size
    @property
    def size(self):
        """Gets size

        Returns:
            int: The size of the square
        """
        return self.__size
    @size.setter
    def size(self, value):
        """Gets the size

        Args:
            value (int): The value to be assigned to size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """Calculates the area of the Square

        Returns:
            int: The area of the Square
        """
        return self.__size ** 2
