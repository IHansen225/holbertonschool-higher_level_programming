#!/usr/bin/python3
""" unittest for Ex6 """


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def maxAtEnd(self):
        self.assertEqual(max_integer([1, 2, 3, 4], 4))

    def maxAtBeg(self):
        self.assertEqual(max_integer([5, 2, 3, 4], 5))

    def maxAtMid(self):
        self.assertEqual(max_integer([5, 2, 6, 3, 4], 6))

    def negExists(self):
        self.assertEqual(max_integer([5, -4, 6, 3, 4], 6))

    def allNeg(self):
        self.assertEqual(max_integer([-5, -4, -6, -3, -4], -3))

    def oneElement(self):
        self.assertEqual(max_integer([5], 5))

    def noElement(self):
        self.assertEqual(max_integer([], None))

if __name__ == '__main__':
    unittest.main()
