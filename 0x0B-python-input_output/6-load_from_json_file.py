#!/usr/bin/python3

"""module to create an object from a json file
"""

import json


def load_from_json_file(filename):
    """create an object from a json file

    Args:
        filename (file): json file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
