#!/usr/bin/python3

"""module to implement pascal's triangle
"""


def pascal_triangle(n):
    """returns a list of list of integers
    that represent the pascal's triangle

    Args:
        n (int): number of rows
    """
    my_list = []

    if n > 0:
        for row in range(n):
            row_list = []
            for column in range(row + 1):
                if column == 0 or column == row:
                    row_list.append(1)
                else:
                    row_list.append(my_list[row - 1][column] +
                                    my_list[row - 1][column - 1])
            my_list.append(row_list)

    return my_list
