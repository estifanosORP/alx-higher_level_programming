#!/usr/bin/python3
"""
module to check the type of an object
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of, or
    if the object is an instance of a class that it was
    inherited from
    """
    return isinstance(obj, a_class)
