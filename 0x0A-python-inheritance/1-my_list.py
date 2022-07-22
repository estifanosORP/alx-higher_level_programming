#!/usr/bin/python3
"""
module for a class that inherits from the class object
"""


class MyList(list):
    """class inherits from the class object"""
    def __init__(self):
        """initializes the class"""
        super().__init__()

    def print_sorted(self):
        """
        prints the list but in ascending order.
        The elements of the list are int
        """
        lst_cpy = self[:]
        lst_cpy.sort()
        print(lst_cpy)
