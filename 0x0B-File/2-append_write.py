#!/usr/bin/python3

"""
Created by Samuel Ezeh
28th sept 2022
THis module creates a a function that appends a string at
the end of a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    append_write appends a string at the end of a text file

    Arguments:
        filename (str): Name of the file
        text (str): The string to appd to file
    """
    with open(filename, mode="a", encoding="UTF8") as file:
        return (file.write(text))
