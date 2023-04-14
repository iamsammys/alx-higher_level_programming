#!/usr/bin/python3

"""module to implement a class Student
"""

import json


class Student:
    """a class Student
    """
    def __init__(self, first_name, last_name, age):
        """initialises the instances

        Args:
            first_name (str): the first name of Student
            last_name (str): last name of Student
            age (int): age of Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves the dictionary representation of Student

        Returns:
            dictionary representation of the class
        """
        return self.__dict__
