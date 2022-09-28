#!/usr/bin/python3
""" rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle subclass """
    __width = None
    __height = None
    
    def __init__(self, width, height):
        """ init function """
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
