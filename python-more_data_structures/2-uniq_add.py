#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return 0
    nl = list(dict.fromkeys(my_list))
    s = 0
    for i in range(len(nl)):
        s += nl[i]
    return s
