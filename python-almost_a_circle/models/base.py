#!/usr/bin/python3
"""
Project: "Almost a circle"
File contents: Base class constructor and methods
"""


class Base():
    """
    Base class

    __nb_objects: generic ID for unidentified objects assigned when ID is None
    id: unique identifier for objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init function // constructor """
        Base.__nb_objects += 1 if id is None else 0
        self.id = self.__nb_objects if id is None else id
