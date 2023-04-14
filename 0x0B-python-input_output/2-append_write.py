#!/usr/bin/python3

"""module to append string to a file
"""


def append_write(filename="", text=""):
    """appends a string to a file

    Args:
        filename (file): the file to append to
        text (str): the text to append to the file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
