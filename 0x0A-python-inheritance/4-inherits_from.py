#!/usr/bin/python3

"""
module that defines a fun that checks
if an object is inhertied from a speficied class
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is of a class that
    iherits from a specified class
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
