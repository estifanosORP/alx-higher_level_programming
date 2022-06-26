#!/usr/bin/python3.py

"""
Defines a class square
"""


class Square:
    """
    A class object for square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        returns the size of the square
        """
        return self.__size

    @property
    def position(self):
        """
        returns the position of the space
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        setter for the private attribute position
        """
        if type(value) != tuple or len(value) != 2:
            error = "position must be a tuple of 2 positive integers"
            raise TypeError(error)
        elif type(value[0]) != int or type(value[1]) != int:
            error = "position must be a tuple of 2 positive integers"
            raise TypeError(error)
        elif value[0] < 0 or value[1] < 0:
            error = "position must be a tuple of 2 positive integers"
            raise TypeError(error)
        else:
            self.__position = value

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
            return

        for i in range(self.__position[1]):
            print("")

        for x in range(self.__size):
            print(" "*self.__position[0], end='')
            print('#'*self.__size, end='')
            print("")

    def __str__(self):
        """
        method to define the string to print 
        when the function print() is called on the object
        """
        if (self.__size == 0):
            return ""

        print_1 = ["\n" for i in range(self.__position[1])]
        print_2 = [" "*self.__position[0] + "#"*self.__size + '\n'
                   for i in range(self.__size)]

        tobe_printed = "".join(print_1) + "".join(print_2)[:-1]
        return tobe_printed
