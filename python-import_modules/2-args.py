#!/usr/bin/python3
if __name__ == "__main__":
    import sys as s
    pl = "s" if len(s.argv) > 1 else ""
    print("{} argument{}:")
    for i in range(len(s.argv) + 1):
        print("{}: {}".format(i, s.argv[i]))
