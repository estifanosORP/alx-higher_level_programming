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
