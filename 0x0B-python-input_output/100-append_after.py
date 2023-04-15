#!/usr/bin/python3

"""module to inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after
    each line containing a specific string

    Args:
        filename (file): file to modify
        search_string (str): string to find
        new_string (str): string to append
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for index, string in enumerate(lines):
            if search_string in string:
                lines.insert((index + 1), new_string)

        new_str = "".join(lines)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(new_str)
