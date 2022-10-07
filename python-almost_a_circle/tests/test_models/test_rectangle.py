#!/usr/bin/python3
""" unittest for Base class """
import unittest
from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):

    def test_rectID(self):
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(r.id, 1)

    def test_params(self):
        r0 = Rectangle(1, 2)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)

        r1 = Rectangle(1, 2, 3)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)

    def test_neg_in_args(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -1)

    def test_print(self):
        r4 = Rectangle(1, 1, 1, 1, 89)
        self.assertEqual(print(r4), "[Rectangle] (89) 1/1 - 1/1")

    def test_str_in_args(self):
        with self.assertRaises(TypeError):
            Rectangle("a", 1)
        with self.assertRaises(TypeError):
            Rectangle(1, "a")
        with self.assertRaises(TypeError):
            Rectangle(1, 1, "a")
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, "a")
        
    def test_zero_in_args(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_neg_in_pos_args(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1)

    def test_area(self):
        r3 = Rectangle(1, 1)
        self.assertEqual(r3.area(), 1)
