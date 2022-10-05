#!/usr/bin/python3
"Initializes the Base class"
import json


class Base:
    "Base class"
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        "Returns the JSON string representation of a list of dictionaries"
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(f"{cls.__name__}.json", 'w', encoding='utf-8') as f:
            if not list_objs:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        "Returns an instance of any Base subclass with all attributes set"
        if cls.__name__ == "Square":
            inst = cls(10)
        else:
            inst = cls(10, 10)
        inst.update(**dictionary)
        return inst
