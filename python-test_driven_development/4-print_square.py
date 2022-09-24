#!/usr/bin/python3
"""" print square function """


def print_square(size):
    """ print square """
    if type(size) is not int or type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    sq = [["#" for i in range(size)] for j in range(size)]
    for i in range(size):
        print("".join(sq[i]))
