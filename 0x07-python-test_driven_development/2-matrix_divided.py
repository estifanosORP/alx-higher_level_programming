#!/usr/bin/python3
"""
Module for matrix division
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix

    Args:
        matrix: list of lists (all elements must be ints or floats)
        div: divisor number
    Returns:
        A new matrix that is the result of the element-wise division
    """
    if (not isinstance(matrix, list) or matrix == []):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of"
                            " integers/floats")
        for num in row:
            if type(num) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of"
                                " integers/floats")

    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    for row in matrix:
        row_div = []
        for elem in row:
            row_div.append(round(elem/div, 2))
        result.append(row_div)
    return result
