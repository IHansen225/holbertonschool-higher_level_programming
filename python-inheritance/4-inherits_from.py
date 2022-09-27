#!/usr/bin/python3
""" check subclass module """


def inherits_from(obj, a_class):
    """ check inheritance of a class """
    return issubclass(a_class, type(obj))
