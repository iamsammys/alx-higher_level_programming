#!/usr/bin/python3

"""module to deserialise an object to json
"""

import json


def from_json_string(my_str):
    """returns deserialised string from json

    Args:
        my_str (str): string to deserialise

    Returns:
        string from json
    """
    return json.loads(my_str)
