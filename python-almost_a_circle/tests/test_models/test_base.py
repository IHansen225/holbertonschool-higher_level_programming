#!/usr/bin/python3
""" unittest for Base class """


import unittest
from models.base import Base

class Test_classBase(unittest.TestCase):
    
    def test_autoID(self):
        """ check automatic ID assignment """
        b = Base()
        self.assert_equal(b.id, 1) 

if __name__ == '__main__':
    unittest.main()