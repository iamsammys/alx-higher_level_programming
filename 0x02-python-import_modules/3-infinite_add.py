#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    result = 0
    for index, arg in enumerate(argv):
        if index != 0:
            result += int(arg)
    print("{:d}".format(result))
