#!/usr/bin/python3
"""1. Write to a file"""


def write_file(filename="", text=""):
    """function that write a string to a text file,
    and return the number of char written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
