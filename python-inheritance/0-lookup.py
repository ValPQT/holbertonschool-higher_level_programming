#!/usr/bin/python3
def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Return:
        A list of strings containing the names of the object's
        attributes and methods.
    """
    return dir(obj)
