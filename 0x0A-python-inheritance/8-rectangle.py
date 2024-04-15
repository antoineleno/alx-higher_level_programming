#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle

    Args:
        BaseGeometry (base class): base class
    """    
    def __init__(self, width, height):
        """contructor method

        Args:
            width (int): width of the rectange
            height (int): height of the rectange
        """        
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
