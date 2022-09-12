#!/usr/bin/python3
def no_c(my_string):
    nst = ""
    for i in range(len(my_string)):
        if my_string[i] not in {"c", "C"}:
            nst = nst + my_string[i]
    return nst
