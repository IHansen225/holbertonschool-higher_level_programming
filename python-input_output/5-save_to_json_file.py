#!/usr/bin/python3
""" save JSON object to file """
import json


def save_to_json_file(my_obj, filename):
    """ save JSON object to file """
    with open(filename, 'a', encoding='utf-8') as f:
        jo = json.dumps(my_obj)
        f.write(jo)
