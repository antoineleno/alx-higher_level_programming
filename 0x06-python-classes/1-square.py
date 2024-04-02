#!/usr/bin/python3
"""Definiton of a class Square that defines

    a square by: (based on 0-square.py)
    """
class Square:
    """A class square
        
        Args:
            size (int): variable size
        
        Return: return the size and the string
    """
    def __init__(self, size):
        self.__size = size

    def __str__(self):
        return f"Square(size={self.__size})"

    def __repr__(self):
        return self.__str__()
