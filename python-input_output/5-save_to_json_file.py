#!/usr/bin/python3
import json

"""
       Writes a Python object to a text file using JSON representation.

       Args:
           my_obj: The Python object to be serialized and written.
           filename: The name of the file to write to.
       """


def save_to_json_file(my_obj, filename):
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
