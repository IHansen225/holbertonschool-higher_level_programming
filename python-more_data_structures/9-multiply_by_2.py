#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nd = a_dictionary.copy()
    for i in nd:
        nd.update({i: nd[i] * 2})
    return nd
