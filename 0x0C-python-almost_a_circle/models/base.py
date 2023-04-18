#!/usr/bin/python3

"""module to implement the class base
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json represention of list dictionaries

        Returns:
            str: json string
        """
        if list_dictionaries is not None and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file
        """
        filename = "{}.json".format(cls.__name__)
        dict_list = []
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is not None and len(list_objs) > 0:
                for objs in list_objs:
                    dict_list.append(objs.to_dictionary())
                json_string = cls.to_json_string(dict_list)
                file.write(json_string)

            else:
                file.write(dict_list)

    @staticmethod
    def from_json_string(json_string):
        """creates a list of the JSON string representation

        Returns:
            a list of dictionary
        """
        if json_string is not None and len(json_string) > 0:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """creates and returns an instance
        with all attributes already set

        Args:
            dictionary (dict): dictionary of the arguments

        Returns:
            instance of the class
        """
        if dictionary is not None and len(dictionary) > 0:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """creates a list of instances from a file

        Returns:
            instances of the class
        """
        filename = "{}.json".format(cls.__name__)
        inst_list = []

        with open(filename, "r", encoding="utf-8") as file:
            json_list = file.read()
            dict_list = cls.from_json_string(json_list)
            for dictionary in dict_list:
                inst_list.append(cls.create(**dictionary))
        return inst_list
