#!/usr/bin/python3
""" save JSON object to file """
import json


def load_from_json_file(filename):
    """ create JSON from file """
    with open(filename, 'r') as f:
        return json.load(f)
