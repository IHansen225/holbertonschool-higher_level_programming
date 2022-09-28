#!/usr/bin/python3
""" square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class inherited from Rectangle """

    def __init__(self, size):
        """ init function """
        self.integer_validator("size", size)
        __size = size
        _Rectangle__width = self.__size
        _Rectangle__height = self.__size

    def area(self):
        return super().area()
