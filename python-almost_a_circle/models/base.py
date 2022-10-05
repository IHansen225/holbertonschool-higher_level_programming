#!/usr/bin/python3
"""
Project: "Almost a circle"
File contents: Base class constructor and methods
"""
import json
from os.path import exists


class Base():
    """
    Base class

    __nb_objects: generic ID for unidentified objects assigned when ID is None
    id: unique identifier for objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init function // constructor """
        Base.__nb_objects += 1 if id is None else 0
        self.id = self.__nb_objects if id is None else id

    def integer_validator(self, name, value):
        """ valdates value inputs and raises exceptions depending on the error """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif name in {"width", "height"} and value <= 0:
            raise ValueError(f"{name} must be > 0")
        elif name in {"x", "y"} and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def to_json_string(list_dictionaries):
        """ returns a json string representation of a list of dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        fn = f"{cls.__name__}.json"
        if list_objs is None or list_objs == []:
            jss = json.dumps("[]")
            with open(fn, "w") as f:
                f.write(jss)
        else:
            for i in range(len(list_objs)):
                list_objs[i] = list_objs[i].to_dictionary()
            jss = json.dumps(list_objs)
            with open(fn, "w") as f:
                f.write(jss)

    def from_json_string(json_string):
        """ returns object loaded from json string input """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dum = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            dum = Square(1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        ilist = []
        if exists(f"{cls.__name__}.json"):
            with open(f"{cls.__name__}.json", "r") as f:
                ob = list(Base.from_json_string(f.read()))
            for i in ob:
                ilist.append(cls.create(**i))
        return ilist
