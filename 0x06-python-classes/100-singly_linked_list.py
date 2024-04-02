"""Definiton of a class Square that defines

    a square by: (based on 6-square.py)
"""
class Node:
    """A clasee Node: that defines a node of a singly linked list
    
        Args:
            data (int): value to be inset
            next_node: next node
    """
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """data function to return the value"""
        return self.__data

    @data.setter
    def data(self, value):
        """Function to set the value
            Args:
                value (int): Value to be set
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node Function to define a node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node Function to set the next node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singley linkedList: A singly linked list to print infos about the list"""
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """sorted inset: Function to sort and inset a node"""
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Function to return the data of the node"""
        if self.head is None:
            return ""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
