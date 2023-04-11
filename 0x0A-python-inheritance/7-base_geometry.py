#!/usr/bin/python3

"""module to implement the class BaseGeometry
"""


class BaseGeometry:
    """class BaseGeometry
    """

    def area(self):
        """implements the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name (str): first arg
            value (int): second arg
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
