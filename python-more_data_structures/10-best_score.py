#!/usr/bin/python3
def best_score(a_dictionary):
    sc = 0
    key = ""
    for i in a_dictionary:
        sc = a_dictionary[i] if a_dictionary[i] > sc else sc
        key = i if a_dictionary[i] > sc else key
    return key
