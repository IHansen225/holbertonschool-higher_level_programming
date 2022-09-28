#!/usr/bin/python3
""" add arguments to list in file """
import sys
import os.path

sjson = __import__('5-save_to_json_file').save_to_json_file
ljson = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
args = sys.argv[1:]
new_list = []

if os.path.exists(filename):
    new_list = ljson(filename)

for item in args:
    new_list.append(item)
ljson(new_list, filename)
