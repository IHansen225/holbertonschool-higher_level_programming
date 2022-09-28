#!/usr/bin/python3
""" converts JSON to dictionary """
import json


def from_json_string(my_str):
    """ conversion function """
    return json.loads(my_str)
