#!/usr/bin/python3
"""
Module to calculate the product of two matrices
"""


def col_getter(matrix, col_idx):
    """
    Function that extracts the columns from a matrix - list of lists
    args:
        matrix: the input matrix
        col_idx: the index of the column to be extracted
    return:
        returns the extracted column as a list
    """
    col = []
    for row in matrix:
        col.append(row[col_idx])
    return col


def dot_prod(vec_a, vec_b):
    """
    multiplies two vectors of equal length
    args:
        - vec_a: the first vector
        - vec_b: the second vector
    return:
        returns the dot product of the two vectors
    """
    prod = 0
    for x, y in zip(vec_a, vec_b):
        prod += x*y
    return prod


def matrix_mul(m_a, m_b):
    """
    Returns the product of two matrixes
    args:
        m_a: the first matrix in the product
        m_b: the second matrix in the product
    return:
        m_a * m_b
    """

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are list of lists
    for ele in m_a:
        if not isinstance(ele, list):
            raise TypeError("m_a must be a list of lists")
    for ele in m_b:
        if not isinstance(ele, list):
            raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Check if the elements are numbers (float or int)
    for lst in m_a:
        for ele in lst:
            if type(ele) not in [int, float]:
                raise TypeError("m_a should only contain integers or floats")
    for lst in m_b:
        for ele in lst:
            if type(ele) not in [int, float]:
                raise TypeError("m_b should only contain integers or floats")

    # Check whether each matrix is a rectangular one
    width = len(m_a[0])
    if len(m_a) != 1:
        for lst in m_a:
            if len(lst) != width:
                raise TypeError("each row of m_a must be of the same size")
    width = len(m_b[0])
    if len(m_a) != 1:
        for lst in m_b:
            if len(lst) != width:
                raise TypeError("each row of m_b must be of the same size")

    # Check if the matrices could be multiplied
    shape_a = (len(m_a), len(m_a[0]))
    shape_b = (len(m_b), len(m_b[0]))
    if shape_a[1] != shape_b[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize the product matrix
    product = [[0 for y in range(shape_b[1])] for x in range(shape_a[0])]

    for row_idx in range(shape_a[0]):
        for col_idx in range(shape_b[1]):
            col = col_getter(m_b, col_idx)
            # print(f"Col {col_idx}: {col}")
            # print(f"Row {row_idx}: {m_a[row_idx]}")
            # print("produt: ", dot_prod(m_a[row_idx], col))
            # print("==============================")
            product[row_idx][col_idx] = dot_prod(m_a[row_idx], col)

    return product
