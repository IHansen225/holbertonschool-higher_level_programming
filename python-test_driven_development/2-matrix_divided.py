#!/usr/bin/python3
""" matrix division function """


def matrix_divided(m, div):
    """ divides alle elements from a matrix """
    rl = len(m[0])
    nmat = m.copy()
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    for i in range(len(m)):
        if len(m[i]) != rl:
            raise TypeError("Each row of the matrix must have the same size")
            return
        for j in range(len(m[i])):
            if type(m[i][j]) is not int and type(m[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                return
            nmat[i][j] = m[i][j] / div
    return nmat
