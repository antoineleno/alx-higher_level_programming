#!/usr/bin/python3
"""inheritats_from module"""


def inherits_from(obj, a_class):
    """inherits: Function that check if an instance is a subclass
    Args:
        obj (object): object created from a_class
        a_class (class): base class
    Return:
        True if the case othewise False
    """

    return any(issubclass(type(obj), cls) for cls in a_class.__subclasses__())
