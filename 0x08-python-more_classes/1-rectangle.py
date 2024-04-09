#!/usr/bin/python3
"""Definiton of a class rectable that defines a rectangle

    a rectangle by: (based on 0-rectangle.py)
"""
class Rectangle:
    """A class rectangle
    
        Args:
            width (int): width of the rectangle
            height (int) : height of the rectangle
        Raise:
            Type error and Value error
        Return: The rectangle area
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """A private instance attribute width"""
        return self.__width
    @width.setter
    def width(self, value):
        """Propoerty setter width
            Args:
                value (int): Value to be used
            Return:
                    The width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """A private instance attribute width"""
        return self.__height
    @height.setter
    def height(self, value):
        """Propoerty setter width
            Args:
                value (int): Value to be used
                
            Return:
                    The width
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value          
