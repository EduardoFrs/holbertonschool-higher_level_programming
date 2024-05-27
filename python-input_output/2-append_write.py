#!/usr/bin/python3
"""2. Append to a file"""


def append_write(filename="", text=""):
    """functino that append a str at eof,
    and return number of char written"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
