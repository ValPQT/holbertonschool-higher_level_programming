#!/usr/bin/python3
"""
Defines a class square with size validation and area method
"""
class Square:
    """represents a square """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = int

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2
