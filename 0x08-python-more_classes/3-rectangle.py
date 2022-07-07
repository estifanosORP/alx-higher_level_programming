#!/usr/bin/python3
"""Module for class that creates a rectangle object"""


class Rectangle:
    """An empty rectangle class"""
    def __init__(self, width=0, height=0):
        """Initilizes the rectangle object"""
        self.width = width
        self.height = height

    def __str__(self):
        """printable string representation of the rectangle object"""
        to_print = ""
        if (self.__width == 0 or self.__height == 0):
            return to_print
        for x in range(self.__height):
            to_print = to_print + "#"*self.__width + "\n"
        return to_print[:-1]

    @property
    def width(self):
        """Returns the private property width of the object instance"""
        return self.__width

    @property
    def height(self):
        """Returns the private property height of the object instance"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """calculates the area of the rectangle instance"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of the rectangle instance"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return 2*(self.__width + self.__height)

