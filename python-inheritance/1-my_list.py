#!/usr/bin/python3
""" subclass module """


class MyList(list):
    """ subclass """
    def print_sorted(self):
        """ print sorted list """
        sl = self.copy()
        sl.sort()
        print(sl)
        return sl
