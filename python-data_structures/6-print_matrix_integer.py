#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("\n")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            s = " " if j != len(matrix[i]) - 1 else "\n"
            print("{:d}".format(matrix[i][j]), end=s)
