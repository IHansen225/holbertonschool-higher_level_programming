#!/usr/bin/python3
""" unittest for Base class """


import unittest
from models.base import Base

class Test_classBase(unittest.TestCase):

    def test_autoID(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

if __name__ == '__main__':
    unittest.main()