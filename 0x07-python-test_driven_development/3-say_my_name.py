#!/usr/bin/python3
"""say_my_name function that print a message"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name : function to print the name
        Args:
            first_name (string): first name of the person
            last_name  (string) : last name of the person
        Raises:
            TypeError: if first_name or last_name is not a string
            
        Return:
            No value to be returned
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/3-say_my_name.txt')
