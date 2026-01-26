#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

        @property
        def size(self):
            return self.__size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = int

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

