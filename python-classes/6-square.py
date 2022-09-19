#!/usr/bin/python3

""" class """

class Square:
    __size = None
    __position = None

    """ init function """
    def __init__(self, size=0, position=(0, 0)):
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if position is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (isinstance(position[0], int) and (isinstance(position[0], int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return (self.__size ** 2)

    def size(self):
        return self.__size

    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        mat = [["#" for i in range(self.__size)] for j in range(self.__size)]
        for i in range(self.__size):
            print("".join(mat[i]))
