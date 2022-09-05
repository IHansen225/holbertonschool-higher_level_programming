#!/usr/bin/python3
if __name__ == "__main__":
	import hidden_4 as hd
	for i in range(len(dir(hd))):
		if dir(hd)[i][1] != "_":
			print("{}".format(dir(hd)[i]))

