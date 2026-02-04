#!/usr/bin/python3
"""
Module inherits_from

This module provides a function to check whether an object
is an instance of a subclass of a given class, but NOT
an instance of the class itself.
"""


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a given class.

    Args:
        obj: The object to check.
        a_class: The reference class.

    Return:
        True if obj is an instance of a subclass of a_class,
        False if obj is an instance of a_class itself or unrelated.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
