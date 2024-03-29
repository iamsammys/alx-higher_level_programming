#!/usr/bin/python3
"""module to find the peak number from a list of numbers
"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers

    Args:
        list_of_integers (list): a list of integers

    Returns:
        the peak number
    """
    if len(list_of_integers) <= 0:
        return None
    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (right + left) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]
