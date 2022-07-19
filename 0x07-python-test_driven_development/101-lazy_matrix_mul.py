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

    return np.matmul(np.array(m_a), np.array(m_b)).tolist()
