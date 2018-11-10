#!/usr/bin/python3
"""Mod file_storage.py - class """
import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    """Class FileStorage - """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """func all - no args"""
        return self.__class__.__objects

    def new(self, obj):
        self.__class__.__objects[obj.__class__.__name__ + "." + str(
            obj.id)] = obj

    def save(self):
        """func save - no args"""
        d = {}
        for k, v in self.__class__.__objects.items():
            d[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as a_file:
            a_file.write(json.dumps(d))

    def reload(self):
        """func reload - no args - deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode="r", encoding='utf-8') as a_file:
                d = json.loads(a_file.read())
            for k, v in d.items():
                self.__class__.__objects[k] = BaseModel(**v)
