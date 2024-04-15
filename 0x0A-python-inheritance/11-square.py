#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Rectangle class."""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Square(Rectangle):
    """Square

    Args:
        Rectangle (class): class inherited
    """    
    def __init__(self, size):
        """init method

        Args:
            size (int): size of the square
        """        
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
    
    def area(self):
        """Area method

        Returns:
            int : The area of the square
        """        
        return self.__size ** 2

    def __str__(self):
        """str method

        Returns:
            Representation of the object
        """        
        return (f"[Square] {self.__size}/{self.__size}")