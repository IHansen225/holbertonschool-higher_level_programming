#!/usr/bin/python3
""" read and print text file """


def read_file(filename=""):
    """ read and print text file """
    with open(filename, "r") as f:
        print(f.read())
