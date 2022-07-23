#!usr/bin/python3
"""
module that defines a square class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class for a square object"""
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """returns the area of the square object"""
        return (self.__size ** 2)

    def __str__(self):
        """function that returns the print representation of the object"""
        return f"[Rectangle] {self.__size}/{self.__size}"
