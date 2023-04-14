#!/usr/bin/python3

"""module to make json representation of an object
"""

import json


def to_json_string(my_obj):
    """returns json string

    Args:
        my_obj (str): the string to convert to json

    Returns:
        str: json string
    """
    return json.dumps(my_obj)
