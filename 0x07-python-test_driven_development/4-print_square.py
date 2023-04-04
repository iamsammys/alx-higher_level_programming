#!/usr/bin/python3

"""A module to implement print_square
"""


def print_square(size):
    """Prints square with "#" character

    Args:
        size (int): the length of the square
    """
    if isinstance(size, int) is True and type(size) is int:
        if size < 0:
            raise ValueError("size must be >= 0")
        string = ""
        string += "\n".join("#" * size for x in range(size))
        print(string)
        return

    raise TypeError("size must be an integer")
