#!/usr/bin/python3
""" text indentation function """

def text_indentation(text):
	""" print two new lines after .?: """
	nstr = ""
	if type(text) is not str:
		raise TypeError("text must be a string")
	for i in range(len(text)):
		if text[i] == " " and text[i - 1] == " " and i != 0:
			pass
		elif text[i] in {'.', '?', ':'}:
			nstr += f"{text[i]}\n\n"
		else:
			nstr += text[i]
	for i in range(len(nstr)):
		if nstr[i] == " " and nstr[i - 1] == "\n" and i != 0:
			pass
		else:
			print(nstr[i], end="")
	print("")
