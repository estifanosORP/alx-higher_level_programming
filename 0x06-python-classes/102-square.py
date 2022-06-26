#!/usr/bin/python3.py

"""
Defines a class square
"""


class Square:
    """
    A class object for square
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        returns the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the property size of the square
        """
        if type(value) == int and value >= 0:
            self.__size = value
        else:
            if type(value) != int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")

    def area(self):
        """
        calculates the area of the square
        """
        return self.__size**2

    def __eq__(self, other):
        """equality comparison"""
        return self.area() == other.area()
    
    def __ne__(self, other):
        """not equal"""
        return self.area() != other.area()

    def __gt__(self, other):
        """greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """greater or equal to"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """less than or equal to"""
        return self.area() <= other.area()
