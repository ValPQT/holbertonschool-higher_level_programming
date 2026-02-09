#!/usr/bin/python3
"""
      Reads a text file (UTF-8) and prints its contents to stdout.

      Args:
          filename (str): The name of the file to read.
      """


def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read())
