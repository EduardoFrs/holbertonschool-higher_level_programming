#!/usr/bin/pyhton3
"""function that print a square"""


def print_square(size):
    """
    print square of size 'size'
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
