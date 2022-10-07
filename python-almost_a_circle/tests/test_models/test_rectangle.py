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

    def test_display_without_xy(self):
        """ check the correct print of the rectangle """
        # without x and y values
        # creating a temporary output
        temp = StringIO()
        # redirect the output to my temporary output
        sys.stdout = temp
        
        rect0 = Rectangle(1, 2)
        rect0.display()
        self.assertEqual(temp.getvalue(), "#\n#\n")

        # without y value
        temp = StringIO()
        sys.stdout = temp

        rect1 = Rectangle(1, 2, 3)
        rect1.display()
        self.assertEqual(temp.getvalue(), "   #\n   #\n")

        # with x and y values
        temp = StringIO()
        sys.stdout = temp

        rect2 = Rectangle(2, 2, 2, 1)
        rect2.display()
        self.assertEqual(temp.getvalue(), "\n  ##\n  ##\n")

    def test_to_dictionary(self):
        """ check the correct return of the to_dictionary method """
        rect = Rectangle(1, 2, 3, 0, 8)
        result = {'x': 3, 'y': 0, 'id': 8, 'height': 2, 'width': 1}
        self.assertEqual(rect.to_dictionary(), result)

    def test_update(self):
        """ check the correct update of attributes """
        rect = Rectangle(1, 1, 1, 1, 1)

        rect.update(2)
        self.assertEqual(rect.__str__(), '[Rectangle] (2) 1/1 - 1/1')

        rect.update(height=3, width=4, x=5, y=6)
        self.assertEqual(rect.__str__(), '[Rectangle] (2) 5/6 - 4/3')

    def test_create_method(self):
        """ check the correct creation of a new instance """
        rect0 = Rectangle.create(**{ 'id': 89 })
        self.assertEqual(rect0.id, 89)

        rect1 = Rectangle.create(**{'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(rect1.id, 5)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect1.x, 3)
        self.assertEqual(rect1.y, 4)

    def test_save_to_file(self):
        """ check the correct functionality of the save_to_file method """