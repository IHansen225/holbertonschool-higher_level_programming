#!/usr/bin/python3
def print_matrix_integer(mat=[[]]):
    if len(mat[0]) == 0:
        print("\n")
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print("{:d}".format(mat[i][j]), end=" " if j + 1 != len(mat[i]) else "\n")
