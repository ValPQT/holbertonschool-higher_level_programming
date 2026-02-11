#!/usr/bin/python3
"""
This module provides a function that appends a string
to the end of a UTF-8 encoded text file.
"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
