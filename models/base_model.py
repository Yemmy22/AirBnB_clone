#!/usr/bin/python3
'''
A BaseModel Module.
'''

from datetime import datetime
import uuid
from models.__init__ import storage


class BaseModel():
    '''
    A BaseModel class. This will be the base class for all
    child classes.
    '''

    def __init__(self, *args, **kwargs):
        '''
        Class constructor. Initializes instances of BaseModel
        class and assigns public attributes.
        '''
        if kwargs:
            for att in kwargs.keys():
                if att != "__class__":
                    setattr(self, att, kwargs[att])
                if att == "created_at" or att == "updated_at":
                    setattr(self, att, datetime.fromisoformat(kwargs[att]))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        '''
        Modifies and return the string representation of the
        BaseModel object.
        '''
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''
        Updates the update_at attribute of the object
        and saves the object to a file.
        '''
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        '''
        Appends the object class name to the object dict
        and returns the updated dict object.
        '''
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
