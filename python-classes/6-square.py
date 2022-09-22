#!/usr/bin/python3
""" class """


class Square:
    """class attributes"""

    __size = None
    __position = None

    """ init function """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            mat = [[" " for i in range(self.__position[0])] for j in range(self.__size)]
            for i in range(self.__size):
                mat[i] = mat[i] + ["#" for i in range(self.__size)]
            for i in range(self.__size):
                print("".join(mat[i]))