#!/usr/bin/python3
"""
This module provides a function that appends a string
to the end of a UTF-8 encoded text file.
"""
import json

"""
       Returns the JSON representation of an object.

       Args:
           my_obj: The Python object to convert to a JSON string.

       Return:
           A string containing the JSON representation of my_obj.
       """


def to_json_string(my_obj):
    return json.dumps(my_obj)
