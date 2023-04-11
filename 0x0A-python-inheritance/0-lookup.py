#!/usr/bin/python3

"""A nodule that implements return of list of
available attributes and methods of an object
"""


def lookup(obj):
    return dir(obj)
