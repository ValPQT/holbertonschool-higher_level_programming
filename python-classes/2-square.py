#!/usr/bin/python3
"""
Defines a class square
"""
class Square:
    """ represents a square """
    def __init__(self, size=0):
        self.__size = int
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        print(size)

