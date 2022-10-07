#!/usr/bin/python3
""" unittest for Base class """


import unittest
from models.base import Base

class BaseClassTest(unittest.TestCase):
    
    def test_autoID(self):
        b = Base()
        self.assert_equal(b.id, 0) 

if __name__ == '__main__':
    unittest.main()