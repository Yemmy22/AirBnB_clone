#!/usr/bin/python3
'''
A Place Test Module.
'''

import unittest
from models.base_model import BaseModel
from models.place import Place
import uuid


class test_Place_FileStorage(unittest.TestCase):
    '''
    Subclass of unittest.Testcases. Performs unittest on
    all instances of Place class.
    '''
    def setUp(self):
        '''
        Defines the test attributes.
        '''
        my_model = Place()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.obj = my_model

        self.obj_str = self.obj.__str__()
        self.time_0 = self.obj.updated_at

    def test_issubclass(self):
        '''
        Tests that Place is a subclass of BaseModel.
        '''
        self.assertTrue(Place, BaseModel)

    def test_instance(self):
        '''
        Test that the object is an instance of Place.
        '''
        self.assertIsInstance(self.obj, Place)
        name = "base1"
        arg = name
        kwargs = {"name": "base2"}

        self.obj1 = Place(*arg, **kwargs)
        self.assertNotEqual(self.obj1.name, "base1")
        self.assertEqual(self.obj1.name, "base2")

    def test_id(self):
        '''
        Test that id is an attribute of the object.
        '''
        self.assertTrue(hasattr(self.obj, "id"))

    def test_created_at(self):
        '''
        Test that created_at is an attribute of the object.
        '''
        self.assertTrue(hasattr(self.obj, "created_at"))

    def test_updated_at(self):
        '''
        Test that updated_at is an attribute of the object.
        '''
        self.assertTrue(hasattr(self.obj, "updated_at"))

    def test_name(self):
        '''
        Test that name is an attribute of the class and object.
        '''
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(self.obj, "name"))
        self.assertIs(type(Place.name), str)

    def test_city_id(self):
        '''
        Test that city_id is an attribute of the class
        and object.
        '''
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(self.obj, "city_id"))
        self.assertIs(type(Place.city_id), str)

    def test_user_id(self):
        '''
        Test that user_id is an attribute of the class
        and object.
        '''
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(self.obj, "user_id"))
        self.assertIs(type(Place.user_id), str)

    def test_description(self):
        '''
        Test that description is an attribute of the class
        and object.
        '''
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(self.obj, "description"))
        self.assertIs(type(Place.description), str)

    def test_number_rooms(self):
        '''
        Test that number_rooms is an attribute of the class
        and object.
        '''
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(self.obj, "number_rooms"))
        self.assertIs(type(Place.number_rooms), int)

    def test_number_bathrooms(self):
        '''
        Test that number_bathrooms is an attribute of the class
        and object.
        '''
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(self.obj, "number_bathrooms"))
        self.assertIs(type(Place.number_bathrooms), int)

    def test_max_guest(self):
        '''
        Test that max_guest is an attribute of the class
        and object.
        '''
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(self.obj, "max_guest"))
        self.assertIs(type(Place.max_guest), int)

    def test_price_by_night(self):
        '''
        Test that price_by_night is an attribute of the class
        and object.
        '''
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(self.obj, "price_by_night"))
        self.assertIs(type(Place.price_by_night), int)

    def test_latitude(self):
        '''
        Test that latitude is an attribute of the class
        and object.
        '''
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(self.obj, "latitude"))
        self.assertIs(type(Place.latitude), float)

    def test_longitude(self):
        '''
        Test that longitude is an attribute of the class
        and object.
        '''
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(self.obj, "longitude"))
        self.assertIs(type(Place.longitude), float)

    def test_amenity_ids(self):
        '''
        Test that amenity_ids is an attribute of the class
        and object.
        '''
        self.assertTrue(hasattr(Place, "amenity_ids"))
        self.assertTrue(hasattr(self.obj, "amenity_ids"))
        self.assertIs(type(Place.amenity_ids), list)

    def test_str(self):
        '''
        Test that the method returns a string object.
        '''
        expected_str = "[Place] ({}) {}"\
            .format(self.obj.id, self.obj.__dict__)
        self.assertEqual(str(self.obj), expected_str)

    def test_save(self):
        '''
        Test that the method updates the update_at attribute's
        timestamp
        '''
        self.obj.save()
        self.time_1 = self.obj.updated_at
        self.assertGreater(self.time_1, self.time_0)

        initial_updated_at = self.obj.updated_at
        self.obj.save()

        self.assertNotEqual(initial_updated_at, self.obj.updated_at)

        loaded_obj = Place(**self.obj.to_dict())
        self.assertEqual(self.obj.id, loaded_obj.id)
        self.assertEqual(self.obj.created_at, loaded_obj.created_at)
        self.assertEqual(self.obj.updated_at, loaded_obj.updated_at)

    def test_to_dict(self):
        '''
        Test that the method contains a keyword "__class__"
        and returns a dictionary.
        '''
        self.dict = self.obj.to_dict()
        self.assertIn("__class__", self.dict)
        self.assertIsInstance(self.dict, dict)

    def test_obj_1_not_obj(self):
        '''
        Test that obj_1 is not obj.
        '''
        obj_dict = self.obj.to_dict()
        new_obj = Place(**obj_dict)
        self.obj_new = new_obj
        self.assertIsNot(self.obj_new, self.obj)

    def test_class_not_attr(self):
        '''
        Test that "__class__" is not an attribute of obj_1
        '''
        self.dict = self.obj.to_dict()
        self.new_obj = Place(**self.dict)
        self.assertNotIn("__class__", self.new_obj.__dict__)

    def test_attr_is_key_value(self):
        '''
        Test that keys in obj dict are attributes of obj_1.
        '''
        self.dict = self.obj.to_dict()
        self.obj_1 = Place(**self.dict)
        for key, value in self.dict.items():
            if key != "__class__":
                with self.subTest(key=key):
                    self.assertIn(key, self.obj_1.__dict__)
