#!/usr/bin/python3
"""
module for a custom class that inherits from
the int class
"""


class MyInt(int):
    """class for a custom int object - MyInt"""
    def __int__(self):
        """initializes the object"""
        super().__init__()

    def __eq__(self, other):
        """method for =="""
        return (int.__ne__(self, other))

    def __ne__(self, other):
        """method for !="""
        return (int.__eq__(self, other))
