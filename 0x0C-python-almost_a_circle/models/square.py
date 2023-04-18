#!/usr/bin/python3

"""a module to implement the Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialises the attributes of Square instances

        Args:
            size (int): size of Square objects
            x (int): attribute of Square objects
            y (int): attribute of the Square instances
            id (int): unique id of instances of the class
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """returns the string representation of an instance

        Returns:
            str: string representation of the instance
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id,
                                             self.x, self.y, self.height)

    def update(self, *args, **kwargs):
        """updates the value of the instances

        Args:
            args (list): a list of arguments
            kwargs (dict): key-worded argument
        """
        if args is not None and len(args) > 0:
            for idx, value in enumerate(args):
                if idx == 0:
                    self.id = value
                if idx == 1:
                    self.size = value
                if idx == 2:
                    self.x = value
                if idx == 3:
                    self.y = value
        elif kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    @property
    def size(self):
        """gets the value of size

        Returns:
            int: size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of size

        Args:
            value (int): value to assign to size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = self.height = value

    def to_dictionary(self):
        """ returns the dictionary representation of the instance

        Returns:
            dict: dictionary implementation of instance
        """
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}

    def to_csv(self):
        """Creates a list with Square attributes

        Returns:
            A Square attributes' list for csv file
        """
        return [self.id, self.size, self.x, self.y]
