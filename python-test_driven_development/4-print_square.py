#!/usr/bin/python3
"""" print square function """


def print_square(size):
	if type(size) is not int or type(size) is float and size < 0:
		raise TypeError("size must be an integer")
	elif size < 0:
		raise ValueError("size must be >= 0")
	if size == 0:
		print("")
	sq = [["#" for i in range(size)] for j in range(size)]
	for i in range(size):
		print("".join(sq[i]))
