#!/usr/bin/python3
"""9-student"""


class Student:
    """Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json

        Returns:
            dictionary_repr:dictionarry representation of the class
        """
        return self.__dict__
