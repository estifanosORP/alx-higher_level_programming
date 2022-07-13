#!/usr/bin/python3

"""
module that prints a square
"""


def print_square(size):
    """
    prints a square with the character #
    """

    if (not isinstance(size, int)) or (isinstance(size, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        print("#"*size)
