#!/usr/bin/python3
"""
module that manipulates the attributes of a class
"""


def add_attribute(obj, att_name, att_value):
    """
    function that adds a new attribute to an object if it's
    possible
    args:
        obj: an instance of an object
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, att_name, att_value)
