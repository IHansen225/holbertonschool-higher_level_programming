#!/usr/bin/python3
""" student class with function """


class Student():
    """ student class """

    def __init__(self, first_name, last_name, age):
        """ init function//constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__.copy()
        else:
            self.__dict__.copy().get(attrs)
