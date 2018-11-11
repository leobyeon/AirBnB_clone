#!/usr/bin/python3
"""Mod file_storage.py - class FileStorage - func all, new, save, reload"""
import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    """Class FileStorage - serializes instances to a JSON file and deserializes
     JSON file to instances - Private class attributes __file_path:
    string - path to the JSON file, __objects: dictionary - empty but will
    store all objects by <class name>.id"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """func all - no args - returns the dictionary __objects"""
        return self.__class__.__objects

    def new(self, obj):
        """func new - obj - sets in __objects the obj with key
        <obj class name>.id"""
        self.__class__.__objects[obj.__class__.__name__ + "." + str(
            obj.id)] = obj

    def save(self):
        """func save - no args - serializes __objects to the JSON file
        (path: __file_path)"""
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
