#!/usr/bin/python3
'''
A City module.
'''

from models.base_model import BaseModel
from models.__init__ import storage


class City(BaseModel):
    '''
    A City class, subclass of BaseModel class with
    public class attributes of type string.
    '''

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        '''
        Class constructor inherits BaseModel class constructor.
        Initializes instances of a City.
        '''
        super().__init__(*args, **kwargs)

    def __str__(self):
        '''
        Modifies the string representation of the
        a City. Inherits from the BaseModel class str method.
        '''
        return super().__str__()

    def save(self):
        '''
        Updates the update_at attribute of a City
        and saves the City to a file.
        '''
        super().save()

    def to_dict(self):
        '''
        Appends the City class name to the City's dict object
        and returns the updated object.
        '''
        return super().to_dict()
