#!/usr/bin/python3
"""
Project: "Almost a circle"
File contents: Rectangle class based on the "Base" class
"""
from base import Base


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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
        super().integer_validator("x", x)
        self.__x = x
        super().integer_validator("y", y)
        self.__y = y

    def __str__(self):
        ty = "Square" if isinstance(self, Square) else "Rectangle"
        pos = f"{self.__x}/{self.__y}"
        siz = f"{self.__width}"
        siz += f"/{self.__height}" if ty == "Rectangle" else ""
        return (f"[{ty}] ({self.id}) {pos} - {siz}")

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
        super().integer_validator("width", value)
        self.__width = value
    
    @height.setter
    def height(self, value):
        super().integer_validator("height", value)
        self.__height = value
    
    @x.setter
    def x(self, value):
        super().integer_validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        super().integer_validator("y", value)
        self.__y = value

    def update(self, *args, **kwargs):
        """ updates the corresponding properties from user input """
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.__width = args[1] if len(args) >= 2 else self.__width
            self.__height = args[2] if len(args) >= 3 else self.__height
            self.__x = args[3] if len(args) >= 4 else self.__x
            self.__y = args[4] if len(args) >= 5 else self.__y
        else:
            for k, v in kwargs.items():
                self.id = v if k == "id" else self.id
                self.__width = v if k == "width" else self.__width
                self.__height = v if k == "height" else self.__height
                self.__x = v if k == "x" else self.__x
                self.__y = v if k == "y" else self.__y

    def area(self):
        """ returns the area of the current shape """
        return self.__width * self.__height

    def display(self):
        """ display the shape in a visualization """
        print("\n" * self.__y, end="")
        print(((" " * self.__x) + ("#" * self.__width) + "\n") * self.__height)

    def to_dictionary(self):
        """ returns dictionary representation of the current shape """
        x = f"'x': {self.__x}"
        y = f"'y': {self.__y}"
        id = f"'id': {self.id}"
        width = f"'width': {self.__width}"
        height = f"'height': {self.__height}"
        if isinstance(self, Square):
            dstr = "{" + f"{id}, {x}, {width}, {y}" + "}"
        else:
            dstr = "{" + f"{x}, {y}, {id}, {height}, {width}" + "}"
        return eval(dstr)
