#!/usr/bin/python3

"""A module created by Samuel Ezeh
On the 28th of sept 2022
Creates a function that writes a string to
a text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Function to write a string to a file

    Args:

        filename (str): the name of the file to write

        text (str): the text to be written to the file

    Return: The number of characters written
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        char_len = f.write(text)
        return (char_len)
