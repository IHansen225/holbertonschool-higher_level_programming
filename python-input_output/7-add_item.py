#!/usr/bin/python3
""" add arguments to list in file """
import sys, json, os.path

sjson = __import__('5-save_to_json_file').save_to_json_file
ljson = __import__('6-load_from_json_file').load_from_json_file

fp = "add_item.json"
ls = ljson(fp) if os.path.exists(fp) else []
for i in sys.argv[1:]:
	ls.append(i)
sjson(ls, fp)
