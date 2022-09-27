#!/usr/bin/python3
""" subclass module """


class MyList(list):
    """ subclass """
    def print_sorted(self):
        """ print sorted list """
        self.sort()
        print(self)

