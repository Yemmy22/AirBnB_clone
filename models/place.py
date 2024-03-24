#!/usr/bin/python3
'''
A Place module.
'''

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.__init__ import storage


class Place(BaseModel):
    '''
    A Place class, subclass of BaseModel class with
    public class attributes of string, float and integer types.
    '''

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        '''
        Class constructor inherits BaseModel class constructor.
        Initializes instances of a Place.
        '''
        super().__init__(*args, **kwargs)

    def __str__(self):
        '''
        Modifies the string representation of the
        a Place. Inherits from the BaseModel class str method.
        '''
        return super().__str__()

    def save(self):
        '''
        Updates the update_at attribute of a Place
        and saves the Place to a file.
        '''
        super().save()

    def to_dict(self):
        '''
        Appends the Place class name to the Place's dict object
        and returns the updated object.
        '''
        return super().to_dict()
