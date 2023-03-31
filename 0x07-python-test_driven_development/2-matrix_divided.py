#!/usr/bin/python3

"""A module for manipulating a matrix
"""


def matrix_divided(matrix, div):
    """A function to divide the elements of a matrix

    Args;
        matrix (int): The matrix to be divided
        div (int): The element to divide with

    Return:
        list: a new matrix
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if type(matrix[0]) is list:
        len_list = len(matrix[0])
    for idx in range(len(matrix)):
        if type(matrix[idx]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(matrix[idx]) < len_list:
            raise ValueError("Each row of the matrix must have the same size")
        for num in matrix[idx]:
            if type(num) is not int and type(num) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in lists] for lists in matrix]
