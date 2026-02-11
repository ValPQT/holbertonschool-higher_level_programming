#!/usr/bin/python3
"""
This module provides a function that appends a string
to the end of a UTF-8 encoded text file.
"""


def class_to_json(obj):
    """
    Return the dictionary description of an object for JSON serialization.

    This function takes an object as input and returns its __dict__ attribute,
    which contains all the object's instance attributes. The returned
    dictionary can be easily serialized into JSON format.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing the object's attributes.
    """
    return obj.__dict__
