#!/usr/bin/python3
def uppercase(str):
	newstr = ""
	for i in range(len(str)):
		if 96 < ord(str[i]) < 123:
			newstr = newstr + chr(ord(str[i]) - 32)
		else:
			newstr = newstr + str[i]
	print(f"{newstr}")
