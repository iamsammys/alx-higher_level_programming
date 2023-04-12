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
        """returns the area of Rectangle

        Returns:
            int: area of Rectangle
        """
        return self.__size ** 2
    
    def __str__(self):
        """returns the string representation of Square

        Returns:
            str: str() format
        """
        return "[{}] {}/{}".format(self.__class__.__name__, self.__size, self.__size)
