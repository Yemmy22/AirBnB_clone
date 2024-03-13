#!/usr/bin/python3

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class test_FileStorage(unittest.TestCase):
    '''
    A FileStorage test class. Subclass of unittest.
    '''
    def setUp(self):
        '''
        Creates objects of the FileStorage and BaseModel
        classes.
        '''
        self.storage = FileStorage()
        self.bm_obj = BaseModel()

    def tearDown(self):
        '''
        Cleans up the environment.
        '''
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_storage(self):
        '''
        Test instantiation of Filestorage.
        '''
        self.assertIsInstance(self.storage, FileStorage)

    def test__file_path(self):
        '''
        Test the FileStorage "__file_path" private attribute
        and type.
        '''
        self.assertFalse(hasattr(FileStorage, "__file_path"))
        self.assertIsInstance(self.storage._FileStorage__file_path, str)
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        '''
        Test the FileStorage "__objects" private attribute
        and type.
        '''
        self.assertFalse(hasattr(FileStorage, "__objects"))
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        '''
        Test the FileStorage "all()" method and its return
        value.
        '''
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertIs(self.storage.all(), self.storage._FileStorage__objects)

    def test_new(self):
        '''
        Test that FileStorage "new()" method sets __object
        attribute with the new BaseModel object.
        '''
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertIn(self.bm_obj, self.storage._FileStorage__objects.values())
        self.storage.new(self.bm_obj)
        self.assertIn(self.bm_obj, self.storage.all().values())

    def test_save(self):
        '''
        Tests "save()" methods of FileStorage and BaseModel classes.
        '''
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertIsNotNone(self.bm_obj.created_at)
        self.bm_obj.save()
        self.assertIsNotNone(self.bm_obj.created_at)

        obj = BaseModel()
        obj.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))


    def test_reload(self):
        '''
        Tests "reload()" method of FileStorage reloads the
        same BaseModel object.
        '''
        self.assertTrue(hasattr(FileStorage, "reload"))
        self.bm_obj.name = "same"
        self.bm_obj.save()
        self.storage.reload()
        for obj in self.storage.all().values():
            if obj == self.bm_obj:
                self.assertEqual(obj.name, "same")

        obj = BaseModel()
        obj.save()
        obj_id = obj.id
        obj_created_at = obj.created_at
        obj_updated_at = obj.updated_at
        self.storage.reload()
        loaded_obj = self.storage.all()[f"BaseModel.{obj_id}"]
        self.assertEqual(loaded_obj.id, obj_id)
        self.assertEqual(loaded_obj.created_at, obj_created_at)
        self.assertEqual(loaded_obj.updated_at, obj_updated_at)
