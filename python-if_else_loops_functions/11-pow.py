#!/usr/bin/python3
def pow(a, b):
    res = 1
    while b != 0:
        if b > 0:
            res *= a
            b -= 1
        else:
            res /= a
            b += 1
    return res

