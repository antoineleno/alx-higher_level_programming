#!/usr/bin/python3
"""100-magic_string"""


def magic_string():
    """magic string
        Return:
            return the string
    """
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
