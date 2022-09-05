#!/usr/bin/python3
if __name__ == "__main__":
    import sys as s
    if len(s.argv) == 1:
        print("0 arguments.")
    else:
        pl = ":" if len(s.argv) == 2 else "s:"
        print("{} argument{}".format(len(s.argv) - 1, pl))
        for i in range(1, len(s.argv)):
            print("{}: {}".format(i, s.argv[i]))
    
