#!/usr/bin/python3

"""A module for the class Square
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
            int: The size of the Square
        """
        return self.__size
    @size.setter
    def size(self, value):
        """Sets Size
        
        Args:
            value (int): The value to assign to the size
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
            int: Area of the Square
        """
        return self.__size ** 2
    def my_print(self):
        """Prnts a square representation of the class using '#'
        """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                print("".join(["#" for x in range(self.__size)]))
