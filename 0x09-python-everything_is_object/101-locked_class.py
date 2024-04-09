#!/usr/bin/python3
"""100-locked_class"""


class LockedClass:
    """locked class"""
    __slots__ = ['first_name']


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/101-locked_class.txt')
