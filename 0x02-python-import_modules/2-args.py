#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    arg_str = "arguments"
    if argc == 1:
        arg_str = "argument"
    print("{:d} {:s}{:s}".format(argc, arg_str, ":" if argc > 0 else ""))
    for index, arg in enumerate(argv):
        if index != 0:
            print("{}: {}".format(index, arg))
