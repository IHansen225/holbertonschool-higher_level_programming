#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    ns = set().union(set_2.difference(set_1)).union(set_1.difference(set_2))
    return ns
