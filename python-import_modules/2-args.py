#!/usr/bin/python3
if __name__ == "__main__":
    import sys as s
    pl = "s" if len(s.argv) > 1 else ""
    print("{} argument{}:".format(len(s.argv), pl))
    for i in range(1, len(s.argv)):
        print("{}: {}".format(i, s.argv[i]))
