#!/usr/bin/python3

"""module to implement the class base
"""


class Base:
    """class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialises the class instances

        Args:
            id (int): the unique id of the object of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
