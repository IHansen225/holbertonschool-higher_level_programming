#!/usr/bin/python3
def pow(a, b):
    res = a
    for i in range(0, abs(b-1)):
        res *= a
    return res
