#!/usr/bin/python3.py

"""
Defines a class square
"""


class Square:
    """
    A class object for square
    """

    def __init__(self, size=0):
        self.__size = size

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

    def my_print(self):
        """
        prints in stdout the square with character #
        """
        if (self.__size == 0):
            print("")
        for x in range(self.__size):
            for y in range(self.__size):
                print('#', end='')
            print("")
