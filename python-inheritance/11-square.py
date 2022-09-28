#!/usr/bin/python3
""" square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class inherited from Rectangle """

    def __init__(self, size):
        """ init function """
        self.integer_validator("size", size)
        super().__init__(size, size)
        __size = size

    def area(self):
        return super().area()

    def __str__(self) -> str:
        return f"[Square] {self.__size} / {self.__size}"
