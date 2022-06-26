#!/usr/bin/python3
"""Module that defines a singly linked list"""


class Node:
    """Class for a node in a singly linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves the attribute data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the data attribute of objects"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """retrieves the attribute next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next_node attribute"""
        if isinstance(value, (type(None), Node)):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """Class for a singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted
        position in the list (increasing order
        """
        new = Node(data=value, next_node=None)

        if self.__head is None:
            new.next_node = None
            self.__head = new

        elif self.__head.data > new.data:
            new.next_node = self.__head
            self.__head = new

        else:
            tmp = self.__head
            while (tmp.next_node is not None
                   and tmp.next_node.data < new.data):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """makes the class printable"""
        tmp = self.__head
        data_val = []
        while (tmp is not None):
            data_val.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(data_val)
