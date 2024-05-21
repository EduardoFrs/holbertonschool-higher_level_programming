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
        if result == '':
            if char == ' ':
                continue
            else:
                result = char
        else:
            if char in ".?:":
                print(result + '\n\n')
            else:
                print(result, end='')
            result = char
    if result != '':
        print(result, end='')
