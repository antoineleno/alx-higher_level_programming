"""Definiton of a class Square that defines

    a square by: (based on 3-square.py)
"""
class Square:
    """A class square
    
        Args:
            size (int): Size to calculate the square
            
        Return: The square area
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Function size to return the value of size"""
        return self.__size
    @size.setter
    def size(self, value):
        """Function size setter to set the value of size 
            base on certains conditions

            Args :
                value (int): Value to be check
            Return: The value set if no exception

            Raise:
                Raise the Type error if the value is not an interger
                Raise the Value error if the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Function areas Function that return the square area"""
    def area(self):
        return self.__size**2
