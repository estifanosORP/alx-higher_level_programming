#!/usr/bin/python3
"""
module that defines the geometrical properties of a rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    class for the rectangle object
    """
    def __init__(self, width, height):
        """initialize the class"""
        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """function that formats how the object is printed"""
        return f"[Rectangle] {self.__width}/{self.__height}"
