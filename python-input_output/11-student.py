#!/usr/bin/python3
""" student class with function """


class Student():
    """ student class """

    def __init__(self, first_name, last_name, age):
        """ init function//constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, at=None):
        if at is None:
            return self.__dict__.copy()
        else:
            dic = {}
            for i in at:
                for k, v in self.__dict__.items():
                    if k == i:
                        dic[k] = v
            return dic

    def reload_from_json(self, json):
        jsd = json.loads(json)
        for k, v in jsd:
            self.k = v
