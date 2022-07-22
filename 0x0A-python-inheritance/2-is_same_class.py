#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    checks if an object is of a specific type
    args:
        obj: object to check
        a_class: candidate type to check
    return:
        True if obj is of type a_class
        False, otherwise
    """
    return isinstance(obj, a_class)
