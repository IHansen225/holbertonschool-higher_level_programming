#!/usr/bin/python3
""" check subclass module """


def inherits_from(obj, a_class):
    """ check inheritance of a class """
    return type(obj) is a_class
