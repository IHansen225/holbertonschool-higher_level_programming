#!/usr/bin/python3
""" rectangle class """


class Rectangle:
    """ class attributes """
    __width = None
    __height = None
    
    def __init__(self, width=0, height=0):
        """ init function // constructor """
        if width < 0:
            raise ValueError("width must be >= 0")
        elif type(width) is not int:
            raise TypeError("width must be an integer")
        else:
            self.__width = width
        if height < 0:
            raise ValueError("width must be >= 0")
        elif type(height) is not int:
            raise TypeError("width must be an integer")
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
