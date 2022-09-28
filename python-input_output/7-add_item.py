#!/usr/bin/python3
""" add arguments to list in file """
import sys, json


def save_to_json_file(my_obj, filename):
    """ save JSON object to file """
    with open(filename, 'w') as f:
        jo = json.dumps(my_obj)
        f.write(jo)

def load_from_json_file(filename):
    """ create JSON from file """
    with open(filename, 'r') as f:
        return json.load(f)

def append_write(argv):
	lf = load_from_json_file("add_item.json")
	for i in range(len(argv)):
		lf.append(argv[i])
	save_to_json_file(lf, "add_item.json")

append_write(sys.argv)

	