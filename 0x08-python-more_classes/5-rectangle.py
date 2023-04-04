#!/usr/bin/python3

"""Module for the implementation of Rectangle
"""


class Rectangle:
    """Class Rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes the class objects

        Args:
            width (int): width of the Rectangle
            height (int): height of Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the value of width

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width

        Args:
            value (int): the value to assign to width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height

        Returns:
            int: height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height to value

        Args:
            value (int): The value assigned to height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of Rectangle

        Returns:
            int: area of Rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of Rectangle

        Returns:
            int: perimeter of Rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Str representation of Rectangle

        Returns:
            char: representation of Rectangle with '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        string += "\n".join("#" * self.__width for x in range(self.__height))
        return string

    def __repr__(self):
        """Returns the repr representation of object

        Return:
            str: the string to get
        """
        return "{}({:d}, {:d})".format(self.__class__.__name__,
                                       self.__width, self.__height)

    def __del__(self):
        """Detects when delete occurs
        """
        print("Bye rectangle...")
