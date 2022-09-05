#!/usr/bin/python3
def pow(a, b):
    res = a
    for i in range(1, b):
        res *= a
    return res
