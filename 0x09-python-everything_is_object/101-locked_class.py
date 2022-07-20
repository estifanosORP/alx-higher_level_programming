#!/usr/bin/python3
"""
module that manages the creation of an object from a class
"""


class LockedClass:
    """Locked class where attributes can't dynamically be added"""
    __slots__ = ['first_name']
