#!/usr/bin/python3
"""
Module my_list

This module defines a class MyList that inherits from the built-in
list class and provides a method to print the list in sorted order.
"""

class MyList(list):
    """
    A class that inherits from the built-in list.

    This class adds a method to display the list elements
    in ascending sorted order without modifying the original list.
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.

        The original list is not modified.
        """
        print(sorted(self))
