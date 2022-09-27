#!/usr/bin/python3
""" check subclass module """


def inherits_from(obj, a_class):
    """ check inheritance of a class """
    return issubclass(type(obj), a_class)
