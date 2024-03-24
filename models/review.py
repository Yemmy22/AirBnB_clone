#!/usr/bin/python3
'''
A Review module.
'''

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.__init__ import storage


class Review(BaseModel):
    '''
    A Review class, subclass of BaseModel class with
    public class attributes of type string.
    '''

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        '''
        Class constructor inherits BaseModel class constructor.
        Initializes instances of a Review.
        '''
        super().__init__(*args, **kwargs)

    def __str__(self):
        '''
        Modifies the string representation of the
        a Review. Inherits from the BaseModel class str method.
        '''
        return super().__str__()

    def save(self):
        '''
        Updates the update_at attribute of a Review
        and saves the Review to a file.
        '''
        super().save()

    def to_dict(self):
        '''
        Appends the Review class name to the Review's dict object
        and returns the updated object.
        '''
        return super().to_dict()
