#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    rv = {
        "M": 1000, "D": 500,
        "C": 100, "L": 50,
        "X": 10, "V": 5, "I": 1
    }
    val_ls = []
    val = 0
    for i in range(len(roman_string)):
        for j in rv.keys():
            if j == roman_string[i]:
                val_ls.append(rv[j])
    i = 0
    while i < len(val_ls):
        if i < len(val_ls) - 1 and val_ls[i] < val_ls[i + 1]:
            val += val_ls[i + 1] - val_ls[i]
            i += 2
        else:
            val += val_ls[i]
            i += 1
    return val
