#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        z = 0
        for i in range(x):
            print(my_list[i], end="")
            z += 1
        print("")
        return z
    except:
        print("")
        return z

