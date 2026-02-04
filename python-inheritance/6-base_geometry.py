#!/usr/bin/python3
"""
Module base_geometry

This module defines the BaseGeometry class with an unimplemented
area method meant to be overridden by subclasses.
"""


class BaseGeometry:
    """
    BaseGeometry class.

    This class serves as a base class for geometric shapes.
    It defines a common interface for calculating area.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method
        has not been implemented.

        This method is meant to be overridden by subclasses.
        """
        raise Exception("area() is not implemented")
