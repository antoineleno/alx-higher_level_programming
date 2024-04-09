#!/usr/bin/python3
"""print_square function"""


def print_square(size):
    """
    print_square: function to print a square with character #
        Args:
            size(int): size of the square
            
        Raises:
            TypeError: if size is not an integer
            or size is less than or equal to zero
            
        Return:
            No value to be returned
        """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
    

if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/4-print_square.txt')
