#!/usr/bin/python3
"""
module for function that describes an object
"""


def lookup(obj):
    """function that returns the list of available and methods of an object"""
    return list(dir(obj))
