#!/usr/bin/python3

"""a module to read a text file
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
        filename (file): the file to read from
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
