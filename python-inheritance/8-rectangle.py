#!/usr/bin/python3
""" rectangle class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
integer_validator = __import__('7-base_geometry').integer_validator

class Rectangle(BaseGeometry):
    """ rectangle subclass """
    __width = None
    __height = None
    
    """ init function """
    def __init__(self, width, height):
        integer_validator("width", width)
        self.width = width
        integer_validator("height", height)
        self.height = height
