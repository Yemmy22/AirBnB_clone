#!/usr/bin/python3
'''
A State module.
'''

from models.base_model import BaseModel
from models.__init__ import storage


class State(BaseModel):
    '''
    A State class, subclass of BaseModel class with
    public class attribute of type string.
    '''

    name = ""

    def __init__(self, *args, **kwargs):
        '''
        Class constructor inherits BaseModel class constructor.
        Initializes instances of a State.
        '''
        super().__init__(*args, **kwargs)

    def __str__(self):
        '''
        Modifies the string representation of the
        a State. Inherits from the BaseModel class str method.
        '''
        return super().__str__()

    def save(self):
        '''
        Updates the update_at attribute of a State
        and saves the State to a file.
        '''
        super().save()

    def to_dict(self):
        '''
        Appends the State class name to the State's dict object
        and returns the updated object.
        '''
        return super().to_dict()
