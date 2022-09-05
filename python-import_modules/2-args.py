#!/usr/bin/python3
if __name__ == "__main__":
    import sys as s
    for i in range(len(s.argv)):
        print("{}: {}".format(i, s.argv[i]))
