#!/usr/bin/python3
"""
This module provides a function that appends a string
to the end of a UTF-8 encoded text file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using JSON representation.

    Args:
        my_obj: The Python object to save.
        filename (str): The name of the file.
    """

    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
