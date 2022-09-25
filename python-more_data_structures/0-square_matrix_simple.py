#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return matrix
    nm = matrix.copy()
    for i in range(0, len(matrix)):
        nm[i] = matrix[i].copy()
        for j in range(0, len(matrix[i])):
            nm[i][j] = nm[i][j] * nm[i][j]
    return nm
