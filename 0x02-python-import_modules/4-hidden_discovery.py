#!/usr/bin/python3
import hidden_4 as hidden
import sys

if __name__ == "__main__":
    for names in dir(hidden):
        if names[0:2] != "__":
            print(names)
