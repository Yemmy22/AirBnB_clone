#!/usr/bin/python3
'''
A User module.
'''

from models.base_model import BaseModel
from models.__init__ import storage


class User(BaseModel):
    '''
    A User class, subclass of BaseModel class with
    public class attributes of type string.
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''
        Class constructor inherits BaseModel class constructor.
        Initializes instances of a User.
        '''
        super().__init__(*args, **kwargs)

    def __str__(self):
        '''
        Modifies the string representation of the
        a User. Inherits from the BaseModel class str method.
        '''
        return super().__str__()

    def save(self):
        '''
        Updates the update_at attribute of a User
        and saves the User to a file.
        '''
        super().save()

    def to_dict(self):
        '''
        Appends the User class name to the User's dict object
        and returns the updated object.
        '''
        return super().to_dict()
