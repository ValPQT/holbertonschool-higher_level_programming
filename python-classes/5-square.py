#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """Define the parameters of the class square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Getter: return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: check if the size is an int and if size >= 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with #"""
        if self.size == 0:
            print("")
        else:
            for _ in range(self.size):
                print("#" * self.size)

