#!/usr/bin/python3
""" save JSON object to file """
import json


def load_from_json_file(filename):
    """ create JSON from file """
    with open(filename, 'a', encoding='utf-8') as f:
        jo = json.dumps(f)
        return jo
