#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for i in range(len(rows)):
            if i != (len(rows)) - 1:
                print("{:d}".format(rows[i]), end=" ")
            else:
                print("{:d}".format(rows[i]), end="")
        print()
