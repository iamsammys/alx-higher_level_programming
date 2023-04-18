#!/usr/bin/python3

"""module to implement the class base
"""

import json
import turtle


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
                json.dump(dict_list, file)

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

        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_list = file.read()
                dict_list = cls.from_json_string(json_list)
                for dictionary in dict_list:
                    inst_list.append(cls.create(**dictionary))
                return inst_list
        except Exception:
            return inst_list

    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.

        Args:
            list_rectangles (list): a list of rectangle instances.
            list_squares (list): a list of square instances.
        """
        t = turtle.Turtle()
        t.screen.bgcolor('#000000')
        t.shape('turtle')
        t.color('#ffffff')
        t.penup()
        t.goto(-200, 200)
        for rect in list_rectangles:
            t.goto(t.xcor() + (rect.width + 20), t.ycor() - (rect.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.penup()

        t.goto(-200, -20)
        for squ in list_squares:
            t.goto(t.xcor() + (squ.width + 20), t.ycor() - (squ.height + 20))
            t.up()
            t.down()
            for i in range(2):
                t.forward(squ.width)
                t.left(90)
                t.forward(squ.height)
                t.left(90)
            t.penup()
        t.Screen().exitonclick()
