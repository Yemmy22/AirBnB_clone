#!/usr/bin/python3
'''
An Amenity module.
'''

from models.base_model import BaseModel
from models.__init__ import storage


class Amenity(BaseModel):
    '''
    An amenity class, subclass of BaseModel class with
    public class attribute of type string.
    '''

    name = ""

    def __init__(self, *args, **kwargs):
        '''
        Class constructor inherits BaseModel class constructor.
        Initializes instances of an Amenity.
        '''
        super().__init__(*args, **kwargs)

    def __str__(self):
        '''
        Modifies the string representation of the
        an Amenity. Inherits from the BaseModel class str method.
        '''
        return super().__str__()

    def save(self):
        '''
        Updates the update_at attribute of an Amenity
        and saves the Amenity to a file.
        '''
        super().save()

    def to_dict(self):
        '''
        Appends the Amenity class name to the Amenity's dict
        object and returns the updated object.
        '''
        return super().to_dict()
