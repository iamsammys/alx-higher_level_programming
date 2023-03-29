#!/usr/bin/python3

"""A module for the class Square
"""


class Square:
    """A class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialises the objects of the class

        Args:
            size (int): The size of the Square
        """
        self.position = position
        self.size = size

    @property
    def position(self):
        """Returns position

        Returns:
            int: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value for position
        Args:
            value (int): the value to assign to position
        """
        if len(value) != 2 or type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for height in range(self.position[1]):
                print()
            for x in range(self.size):
                for length in range(self.position[0]):
                    print(" ", end="")
                print("".join(["#" for x in range(self.size)]))
