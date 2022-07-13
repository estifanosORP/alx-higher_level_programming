#!/usr/bin/python3

"""Module for summing integers"""


def add_integer(a, b=98):
    """
    Sums two integers. If any of the inputs are float, they
    are first casted to ints.
    """

    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
