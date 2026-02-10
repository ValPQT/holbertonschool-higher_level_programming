#!/usr/bin/python3

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
