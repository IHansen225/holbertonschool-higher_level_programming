#!/usr/bin/python3
""" rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle subclass """

    def __init__(self, width, height):
        """ init function """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns area of rectangle """
        return self.__width * self.__height

    def __str__(self) -> str:
        """ returns string representation """
        return f"[Rectangle] {self.__width}/{self.__height}"
