#!/usr/bin/python3
if __name__ == "__main__":
	import calculator_1
	a = 10
	b = 5
	print("{} + {} = {}".format(a, b, sum(a, b)))
	print("{} - {} = {}".format(a, b, sub(a, b)))
	print("{} * {} = {}".format(a, b, mul(a, b)))
	print("{} / {} = {}".format(a, b, div(a, b)))
