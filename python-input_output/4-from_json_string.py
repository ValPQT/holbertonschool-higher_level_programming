#!/usr/bin/python3
import json
"""
    Returns a Python object represented by a JSON string.

    Args:
        my_str: A string containing a JSON representation.

    Return:
        The Python object represented by the JSON string.
    """


def from_json_string(my_str):
    return json.loads(my_str)
