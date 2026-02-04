#!/usr/bin/python3
"""
Module is_kind_of_class

This module provides a function to check whether an object
is an instance of a given class or of a subclass of it.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class or a subclass.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Return:
        True if obj is an instance of a_class or an inherited class,
        False otherwise.
    """
    return isinstance(obj, a_class)

