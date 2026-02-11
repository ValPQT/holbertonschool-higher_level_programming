#!/usr/bin/python3
"""
This module provides a function that appends a string
to the end of a UTF-8 encoded text file.
"""
import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str: A string containing a JSON representation.

    Return:
        The Python object represented by the JSON string.
    """
    return json.loads(my_str)
