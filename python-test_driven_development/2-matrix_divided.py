#!/usr/bin/python3
"""Function for divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    divide all element of a matrix
    return: new matrix with the result of div
    """
    # Check if matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_length = len(matrix[0])

    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
