#!/usr/bin/python3
import json
"""from_json_string: function to convert an object from json string"""


def from_json_string(my_str):
    """from_json_string: function to convert json string to its original object

    Args:
        my_obj (object):
            object to be converted

    Return:
    (object) object representation
    """
    return json.loads(my_str)
