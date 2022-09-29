#!/usr/bin/python3
""" converts JSON to dictionary """
import json


def from_json_string(my_str):
    """ conversion function """
    with open(filename, 'r') as new_obj:
        return json.load(new_obj)
