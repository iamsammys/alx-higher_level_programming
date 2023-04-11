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
