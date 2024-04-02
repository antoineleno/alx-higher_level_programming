"""Definiton of a class Square that defines

    a square by: (based on 4-square.py)
"""
class Square:
    """A class square
    
        Args:
            size (int): Size to calculate the square
            
        Return: The square area
    """
    def __init__(self,size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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
    @property
    def position(self):
        """Function size to return the value of size"""
        return self.__position
    @size.setter
    def position(self, value):
        """Function size setter to set the value of size 
            base on certains conditions

            Args :
                value (int): Value to be check
            Return: The value set if no exception

            Raise:
                Raise the Type error if the value is not an interger
                Raise the Value error if the value is less than 0
        """
        if len(value) != 2 and not isinstance(value, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__position = value
    """Function area that return the square area"""
    def area(self):
        return self.__size**2
    """Function my_print to print in stdout the square with the character #"""
    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size -1:
                print()

    def __str__(self):
        self.my_print()
        return ""

