#!/usr/bin/python3
"""
module that defines the geometry of different shapes
"""


class BaseGeometry():
    """
    Class for the definition of base geometry of different shapes
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
