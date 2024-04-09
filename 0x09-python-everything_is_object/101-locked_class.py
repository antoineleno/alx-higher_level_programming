#!/usr/bin/python3
class LockedClass:
    __slots__ = ['first_name']

if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/101-locked_class.txt')
