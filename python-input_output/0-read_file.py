#!/usr/bin/python3
"""
This module provides a function to read a UTF-8 encoded text file
and print its content to standard output.
"""


def read_file(filename=""):
    """
      Reads a text file (UTF-8) and prints its contents to stdout.

      Args:
          filename (str): The name of the file to read.
      """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read())
