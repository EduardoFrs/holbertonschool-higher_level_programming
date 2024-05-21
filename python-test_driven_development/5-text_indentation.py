#!/usr/bin/python3
"""function that print 2 newline after '., ?, :' char"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':' char
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ''
    for char in text:
        result += char
        if char in ".?:":
            result += '\n\n'

    print(result, end='')
