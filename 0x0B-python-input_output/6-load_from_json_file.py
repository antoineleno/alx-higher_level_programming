#!/usr/bin/python3
"""load_to_json_file"""
import json


def load_from_json_file(filename):
    """save_to_json_file: function to save an object to json file

    Args:
        my_obj (object): object to be converted
        filename (txt): file

    Return:
        the python object loaded from the json file.
    """
    with open(filename, "r") as json_file:
        return json.load(json_file)
