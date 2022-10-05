#!/usr/bin/python3
"""
Project: "Almost a circle"
File contents: Square class based on the "Rectangle" class
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    Square class

    __size: integer value representing the size of the square
    __x: integer value representing the x position of the square
    __y: integer value representing the y position of the square
    id: unique identifier for the square, inherited from Base class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ init function // constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, value):
        super(Square, type(self)).width.fset(self, value)
        super(Square, type(self)).height.fset(self, value)

    def update(self, *args, **kwargs):
        """ updates the corresponding properties from user input """
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            if len(args) >= 2:
                super(Square, type(self)).width.fset(self, args[1])
                super(Square, type(self)).height.fset(self, args[1])
            if len(args) >= 3:
                super(Square, type(self)).x.fset(self, args[2])
            if len(args) >= 4:
                super(Square, type(self)).y.fset(self, args[3])

        else:
            for k, v in kwargs.items():
                self.id = v if k == "id" else self.id
                if k == "size":
                    super(Square, type(self)).width.fset(self, v)
                    super(Square, type(self)).height.fset(self, v)
                if k == "x":
                    super(Square, type(self)).x.fset(self, v)
                if k == "y":
                    super(Square, type(self)).y.fset(self, v)

    def to_dictionary(self):
        return super().to_dictionary()

