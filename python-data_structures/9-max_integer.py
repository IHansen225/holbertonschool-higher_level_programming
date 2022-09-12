#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    mx = my_list[0]
    for i in range(0, len(my_list)):
        mx = my_list[i] if my_list[i] > mx else mx
    return mx
