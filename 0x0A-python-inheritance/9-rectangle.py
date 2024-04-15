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

    def area(self):
        """area: Function to return the area

        Returns:
            string: [Rectangle] <width>/<height>
        """        
        return self.__height * self.__width

    def __str__(self):
        """str method

        Returns:
            Representation of the object
        """        
        return (f"[Rectangle] {self.__width}/{self.__height}")
