#!/usr/bin/python3
"""Function that return the list of available attributes and methods of an object"""
def lookup(obj):
    """Function that returns the list of available attribute

    Args:
        obj (object): object of a class

    Return:
        A list object
    """

    return dir(obj)

