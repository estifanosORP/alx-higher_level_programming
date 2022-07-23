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
    if (
        att_name not in dir(obj) and
        obj.__class__.__module__ != 'builtins' and
        '__slots__' not in dir(obj)
       ):
        setattr(obj, att_name, att_value)
    else:
        raise TypeError("can't add new attribute")
