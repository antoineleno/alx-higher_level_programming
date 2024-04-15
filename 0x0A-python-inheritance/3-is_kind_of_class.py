#!/usr/bin/python3
"""Function to check if an object is an instance of a class """
def is_kind_of_class(obj, a_class):
    """is_kind_of_class

    Args:
        obj (object): object to check
        a_class (class): class 

    Returns:
        boll:
            True of it's an instance otherwise false
    """
    return isinstance(obj, a_class)
