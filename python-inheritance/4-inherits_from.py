#!/usr/bin/python3
""" check subclass module """


def inherits_from(obj, a_class):
    """ check inheritance of a class """
    return isinstance(obj, a_class) and type(obj) is not a_class
