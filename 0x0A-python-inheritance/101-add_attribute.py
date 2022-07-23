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
    try:
        if att_name not in obj.__dict__.keys():
            setattr(obj, att_name, att_value)
    except AttributeError:
        raise TypeError("can't add new attribute")
