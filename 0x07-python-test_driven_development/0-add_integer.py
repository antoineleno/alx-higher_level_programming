#!/usr/bin/python3
"""0-add_integer Function to add two integers."""


def add_integer(a, b=98):
    """
    add_integer Function add integer to add 2 integers together.

    Args:
        a (int or float): First number to be add
        b (int or float): Second number to be add
    Raises:
        TypeError: if a or b is not an int or float
    Return:
        The sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
