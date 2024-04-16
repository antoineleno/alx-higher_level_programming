#!/usr/bin/python3
"""save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file: function to save an object to json file

    Args:
        my_obj (object): object to be converted
        filename (txt): file
    """
    with open(filename, "w") as json_file:
        json.dump(my_obj, json_file)
