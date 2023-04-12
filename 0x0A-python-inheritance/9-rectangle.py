#!/usr/bin/python3

"""module to implement the class Rectangle
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle
    """

    def __init__(self, width, height):
        """initialises the class
        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of Rectangle

        Returns:
            int: area of Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """returns the string representation of Rectangle
        """
        return "[{}] {}/{}".format("Rectangle", self.__width, self.__height)
