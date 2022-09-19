#!/usr/bin/python3
""" class """

class Square:
    __size = None

    """ init function """

    def __init__(self, size = 0) -> None:
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)
