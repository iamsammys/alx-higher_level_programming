#!/usr/bin/python3

"""A module created by Samuel Ezeh
On the 28th of sept 2022
THe module creates a function that reads
a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """A function to read a file and print the contents"""
    with open(filename, encoding="utf-8") as f:
        read_f = f.read()
        print(read_f, end="")
