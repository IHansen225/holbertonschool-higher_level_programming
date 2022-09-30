#!/usr/bin/python3
"""
Project: "Almost a circle"
File contents: Rectangle class based on the "Base" class
"""
Base = __import__('base').Base


class Rectangle(Base):
    """
    Rectangle class

    __width: integer value representing the width of the rectangle
    __height: integer value representing the height of the rectangle
    __x: integer value representing the x position of the rectangle
    __y: integer value representing the y position of the rectangle
    id: unique identifier for the rectangle, inherited from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init function // constructor """
        super().__init__(id)
        __width = width
        __height = height
        __x = x
        __y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        __width = value
    
    @height.setter
    def height(self, value):
        __height = value
    
    @x.setter
    def x(self, value):
        __x = value

    @y.setter
    def y(self, value):
        __y = value
