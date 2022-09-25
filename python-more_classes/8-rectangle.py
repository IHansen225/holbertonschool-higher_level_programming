#!/usr/bin/python3
""" rectangle class """


class Rectangle:
    """ class attributes """
    __width = None
    __height = None
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ init function // constructor """
        Rectangle.number_of_instances += 1
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
        self.print_symbol = Rectangle.print_symbol

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
        ps = str(self.print_symbol)
        if self.__height == 0 or self.__width == 0:
            return ""
        r = [[ps for i in range(self.__width)] for j in range(self.__height)]
        for i in range(len(r)):
            s += "".join(r[i]) + ("\n" if i + 1 != len(r) else "")
        return s

    def __repr__(self) -> repr:
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __print__(self) -> print:
        s = ""
        ps = str(self.print_symbol)
        r = [[ps for i in range(self.__width)] for j in range(self.__height)]
        for i in range(len(r)):
            print("".join(r[i]))
        return s

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
