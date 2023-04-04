#!/usr/bin/python3

"""Created by:
        Samuel Ezeh
"""


def text_indentation(text):
    """prints a text with 2 new lines after
        each of these characters: ., ? and :

    Args:
        text (string): The test to print
    """
    if isinstance(text, str) is False and\
            type(text) is not str:
        raise TypeError("text must be a string")

    string = ""
    for char in text:
        if char in ['.', '?', ':']:
            string += char + '\n\n'
        else:
            string += char
    string = string.replace('\n ', '\n')
    print(string)
