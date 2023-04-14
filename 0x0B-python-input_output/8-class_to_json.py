#!/usr/bin/python3

"""module to create a dictionary description
of an instance for json serialisation
"""


def class_to_json(obj):
    """returns the dictionary description
    with simple data structure

    Returns:
        dictionary for json serialization
    """
    return {key: value for key, value in obj.__dict__.items()}
