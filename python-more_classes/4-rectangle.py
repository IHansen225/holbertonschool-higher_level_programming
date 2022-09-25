#!/usr/bin/python3
""" rectangle class """


class Rectangle:
    """ class attributes """
    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        """ init function // constructor """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self) -> str:
        s = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        r = [["#" for i in range(self.__width)] for j in range(self.__height)]
        for i in range(len(r)):
            s += "".join(r[i]) + ("\n" if i + 1 != len(r) else "")
        return s

    def __repr__(self) -> repr:
        s = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        r = [["#" for i in range(self.__width)] for j in range(self.__height)]
        for i in range(len(r)):
            s += "".join(r[i]) + ("\n" if i + 1 != len(r) else "")
        return s

    def __print__(self) -> print:
        s = ""
        r = [["#" for i in range(self.__width)] for j in range(self.__height)]
        for i in range(len(r)):
            print("".join(r[i]))
        return s

    def __eval__(self, string) -> eval:
        w = 0
        h = 0
        for i in string:
            h = h + 1 if i == "\n" else h
        j = 0
        while string[j] != "\n":
            w += 1
            j += 1
        return Rectangle(w, h)
