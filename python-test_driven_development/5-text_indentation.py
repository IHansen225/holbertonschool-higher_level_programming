#!/usr/bin/python3
""" text indentation function """

def text_indentation(text):
	""" print two new lines after .?: """
	if type(text) is not str:
		raise TypeError("text must be a string")
	for i in text:
		if i in {'.', '?', ':'}:
			print("\n")
		else:
			print(i, end="")
