#!/usr/bin/python3
"""
    Writes a string to a text file (UTF-8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write into the file.

    Returns:
        int: The number of characters written.
    """


def write_file(filename="", text=""):
    with open(filename, mode="w+", encoding="utf-8") as f:
        f.write(text)
        return len(text)
