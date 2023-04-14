#!/usr/bin/python3

"""module to implement a class Student
"""


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

    def to_json(self, attrs=None):
        """retrieves the dictionary representation of Student

        Returns:
            dictionary representation of the class
        """
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items() if key in attrs}
