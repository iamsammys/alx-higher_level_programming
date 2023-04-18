#!/usr/bin/python3

"""module that implements Rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises the class instances

        Args:
            width (int): width of the rectangle instance
            height (int): height of the rectangle object
            x (int): an attribute of the object
            y (int): an attribute of the object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns the value of width

        Returns:
            int: width of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets width with value

        Args:
            value (int): value to assigned to width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the value of height

        Returns:
            int: height of Rctangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets height with value

        Args:
            value (int): height of Rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """return the value of x

        Returns:
            int: value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x to value

        Args:
            value (int): value assigned x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return the value of y

        Returns:
            int: value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y to value

        Args:
            value (int): value assigned y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area of the objects

        Returns:
            int: the value of the area
        """
        return self.__width * self.__height

    def display(self):
        """implements the display of rectangle with #
        """
        if self.__y > 0:
            for empty in range(self.__y):
                print()
        for x in range(self.__height):
            if self.__x > 0:
                print((" " * self.__x), end="")
            print("#" * self.__width)

    def __str__(self):
        """overrides the __str__ function
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates the object attributes

        Args:
            args: a list of arguments
        """
        if args is not None and len(args) != 0:
            for idx, value in enumerate(args):
                if idx == 0:
                    self.id = value
                elif idx == 1:
                    self.width = value
                elif idx == 2:
                    self.height = value
                elif idx == 3:
                    self.x = value
                elif idx == 4:
                    self.y = value

        elif kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns dictionary representation of instances of the class

        Returns:
            dict: the dict format of object
        """
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x,
                "y": self.y}

    def to_csv(self):
        """Creates a list with Rectangle attributes

        Returns:
            A Rectangle attributes' list for csv file
        """
        return [self.id, self.width, self.height, self.x, self.y]
