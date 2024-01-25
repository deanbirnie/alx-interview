#!/usr/bin/python3
"""
Module contains a function that rotates a matrix.
"""


def rotate_2d_matrix(matrix):
    """
    Takes a matrix as an argument and returns the matrix
    but rotated 90 degrees clockwise.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
