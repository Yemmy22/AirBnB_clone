#!/usr/bin/python3
'''
A FileStorage Module.
'''

import json
import os


class FileStorage():
    '''
    A FileStorage class with class attributes to persist all
    objects of the BaseModel class
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Returns all deserialized objects in a dict.
        '''
        return self.__objects

    def new(self, obj):
        '''
        Sets in __objects, an initialized object as the value
        of its class name and id - as key - in in the dictionary.
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''
        Replace objects in __objects with the return value of
        to_dict method and serializes __objects in a file.
        '''
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        '''
        Performs a file check and reloads the into __objects
        deserialzed objects of the BaseModel class, if the
        exists.
        '''
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                try:
                    saved_dict = json.load(f)
                    from models.base_model import BaseModel
                    for name, obj_dict in saved_dict.items():
                        self.__objects[name] = BaseModel(**obj_dict)
                except Exception:
                    pass
