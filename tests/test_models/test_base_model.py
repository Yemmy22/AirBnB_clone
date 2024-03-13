#!/usr/bin/python3
'''
A BaseModel Test Module.
'''


import unittest
from models.base_model import BaseModel
import uuid


class test_BaseModel_FileStorage(unittest.TestCase):
    '''
    Subclass of unittest.Testcases. Performs unittest on
    all instances of BaseModel class.
    '''
    def setUp(self):
        '''
        Defines the test attributes.
        '''
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.obj = my_model

        self.obj_str = self.obj.__str__()
        self.time_0 = self.obj.updated_at

    def test_instance(self):
        '''
        Test that the object is an instance of BaseModel.
        '''
        self.assertIsInstance(self.obj, BaseModel)
        name = "base1"
        arg = name
        kwargs = {"name": "base2"}

        self.obj = BaseModel(*arg, **kwargs)
        self.assertNotEqual(self.obj.name, "base1")
        self.assertEqual(self.obj.name, "base2")

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

    def test_str(self):
        '''
        Test that the method returns a string object.
        '''
        expected_str = "[BaseModel] ({}) {}"\
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

        self.obj = BaseModel()
        initial_updated_at = self.obj.updated_at
        self.obj.save()
        self.assertNotEqual(initial_updated_at, self.obj.updated_at)

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
        new_obj = BaseModel(**obj_dict)
        self.obj_new = new_obj
        self.assertIsNot(self.obj_new, self.obj)

    def test_class_not_attr(self):
        '''
        Test that "__class__" is not an attribute of obj_1
        '''
        self.dict = self.obj.to_dict()
        self.new_obj = BaseModel(**self.dict)
        self.assertNotIn("__class__", self.new_obj.__dict__)

    def test_attr_is_key_value(self):
        '''
        Test that keys in obj dict are attributes of obj_1.
        '''
        self.dict = self.obj.to_dict()
        self.obj_1 = BaseModel(**self.dict)
        for key, value in self.dict.items():
            if key != "__class__":
                with self.subTest(key=key):
                    self.assertIn(key, self.obj_1.__dict__)
