"""Definiton of a class Square that defines

    a square by: (based on 2-square.py)
"""
class Square:
    """A class square
    
        Args:
            size (int): Size to calculate the square
            
        Return: The square area
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        
    def area(self):
        """A function name are
            
            Args: The size
            
            Return: the square area
        """
        return self.__size**2
