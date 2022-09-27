#!/usr/bin/python3
""" subclass module """


class MyList(list):
	""" subclass """
	def print_sorted(self):
		self.sort()
		return self
