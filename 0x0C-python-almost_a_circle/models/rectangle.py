#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """return the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return self.__height * self.__width
    
    def display(self):
        """print the representation of the rectangle"""
        for i in range(self.__y):
            for y in range(self.__x):
                print("", end="")
            print()
        for i in range(self.__height):
            space = self.__x * " "
            print(space, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """return the string representation of the rectangle"""
        rect_repr = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return rect_repr
    
    def update(self, *args, **kwargs):
        """update to update attributes value"""
        if args:
            my_args = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, my_args[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)            

    def to_dictionary(self):
        """return the custom dictionnary representation"""
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}
    
    