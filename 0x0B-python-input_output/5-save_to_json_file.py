#!/usr/bin/python3

"""module to write to a file in json
"""

import json


def save_to_json_file(my_obj, filename):
    """writes json string to a text file

    Args:
        my_obj: object to write to json file
        filename: file to write json object
    
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
