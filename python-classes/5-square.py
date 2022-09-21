#!/usr/bin/python3
""" class """

class Square:
    """class attributes"""
    __size = None

    """ init function """
    def __init__(self, size=0):
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def area(self):
        return (self.__size ** 2)

    @property.read
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            mat = [["#" for i in range(self.__size)] for j in range(self.__size)]
            for i in range(self.__size):
                print("".join(mat[i]))
