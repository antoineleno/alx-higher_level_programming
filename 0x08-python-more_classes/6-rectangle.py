#!/usr/bin/python3
"""Definiton of a class rectable that defines a rectangle

    a rectangle by: (based on 5-rectangle.py)
"""
class Rectangle:
    """A class rectangle
    
        Args:
            width (int): width of the rectangle
            height (int): heigh of the rectangle 
        Raise:
            Type error and Value error
        Return: The rectangle area
    """
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1
    def __del__(self):
        print ("Bye rectangle...")
        Rectangle.number_of_instances -=1
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
    def area(self):
        """area function to return the area"""
        return self.__height * self.__width
    def perimeter(self):
        """perimeter function to return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*(self.__height + self.__width)
    def __str__(self):
        """string method to represente a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for _ in range(self.__height):
            rect_str += '#' * self.__width + '\n'
        return rect_str.rstrip()
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
    
