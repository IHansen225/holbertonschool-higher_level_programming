#!/usr/bin/python3
""" class to JSON """


def class_to_json(obj):
	""" converts class to json object """
	return obj.__dict__

