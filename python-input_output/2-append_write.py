#!/usr/bin/python3
"""
    Appends a string at the end of a text file (UTF-8)
    and returns the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters appended.
    """


def append_write(filename="", text=""):
    with open(filename, mode="a+", encoding="utf-8") as f:
        f.write(text)
        return len(text)
