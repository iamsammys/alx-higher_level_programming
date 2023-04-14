#!/usr/bin/python3

"""module to write to a file
"""


def write_file(filename="", text=""):
    """writes a string to a file

    Args:
        filename (file): the file to write to
        text (str): the text to write to the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
