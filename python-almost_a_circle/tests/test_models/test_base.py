#!/usr/bin/python3
""" unittest for Base class """
import unittest
from models.base import Base


class Test_classBase(unittest.TestCase):

    def test_autoID(self):
        b = Base(id=None)
        self.assertEqual(b.id, 1)
        b0 = Base()
        self.assertEqual(b0.id, 2)

    def test_fID(self):
        b1 = Base(6.9)
        self.assertEqual(b1.id, 6.9)

    def test_opID(self):
        b2 = Base(8 + 9)
        self.assertEqual(b2.id, 17)

    def test_hugeID(self):
        b3 = Base(4e20)
        self.assertEqual(b3.id, 4e20)

    def test_lstID(self):
        b4 = Base([1, 1])
        self.assertEqual(b4.id, [1, 1])

    def test_negID(self):
        b5 = Base(-10)
        self.assertEqual(b5.id, -10)

    def test_strID(self):
        b6 = Base("Betty")
        self.assertEqual(b6.id, "Betty")

    def test_argcount(self):
        with self.assertRaises(TypeError):
            Base(1, 2, 3, 4)

    def test_toJSONstring(self):
        self.assertEqual(Base.to_json_string([{'x': 0}, {'y': 0}]),'[{"x": 0}, {"y": 0}]')
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_fromJSONstring(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])

if __name__ == '__main__':
    unittest.main()