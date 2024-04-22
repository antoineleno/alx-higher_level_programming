#!/usr/bin/python3
"""Class square that inheritate from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = y
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string represenation of an object"""
        sqr_repr = f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        return sqr_repr

    @property
    def size(self):
        """return the size of the square"""
        return self.size

    @size.setter
    def size(self, value):
        """set the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the args and keyword argument"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionnary representation"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
