#!/usr/bin/python3
"""to_json_string: function to convert an object to json string"""
import json


def to_json_string(my_obj):
    """to_son_string: function to convert an object to json string

    Args:
        my_obj (object):
            object to be converted

    Return:
    (JSON) json representation
    """
    return json.dumps(my_obj)
