#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
	try:
		l = 0
		for i in range(x):
			try:
				print("{:d}".format(my_list[i]), end="")
				l += 1
			except:
				pass
		print("")
		return l
	except:
		print("")
		return l
