#!/usr/bin/python3
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
