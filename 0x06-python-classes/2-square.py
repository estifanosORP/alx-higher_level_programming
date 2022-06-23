#!/usr/bin/python3.py

"""
module that defines different objects
"""


class Square:
    """
    A class object for square
    """

    def __init__(self, size=0):
        if type(size) == int and size >= 0:
            self.__size = size
        else:
            if type(size) != int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
