#!/usr/bin/python3
"""
module to multiply to matrices
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    function that multiplies two matrices using the numpy library
    args:
        m_a: first matrix
        m_b: second matrix
    """

    return (np.matmul(m_a, m_b))
