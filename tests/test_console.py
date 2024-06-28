#!/usr/bin/python3

'''
Console Test Module
'''


import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class TestConsole(unittest.TestCase):
    """
    Test all features of the HBNB console: command and
    non-command line arguments.
    """

    def setUp(self):
        """
        Setup before each test
        """
        self.console = HBNBCommand()
        self.models = [BaseModel, User, State, City, Place, Amenity, Review]

    def tearDown(self):
        """
        Clean up after each test
        """
        storage.all().clear()

    def test_do_quit(self):
        """
        Test quit command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual("", f.getvalue().strip())

    def test_do_EOF(self):
        """
        Test EOF command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("EOF")
            self.assertEqual("", f.getvalue().strip())

    def test_help_EOF(self):
        """
        Test help_EOF command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help EOF")
            output_eof = f.getvalue()

            expected_output = 'Quit command to exit the program\n\n'

            self.assertEqual(output_eof, expected_output)

    def test_help_quit(self):
        """
        Test help_EOF command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help quit")
            output_quit = f.getvalue()

            expected_output = 'Quit command to exit the program\n\n'

            self.assertEqual(output_quit, expected_output)

    def test_emptyline(self):
        """
        Test empty line input
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual("", f.getvalue().strip())

    def test_create(self):
        """
        Test create command for each model
        """
        for model in self.models:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("create {}".format(model.__name__))
                model_id = f.getvalue().strip()
                self.assertIn("{}.{}".format(model.__name__, model_id), storage.all().keys())

    def test_show(self):
        """
        Test show command for each model
        """
        for model in self.models:
            instance = model()
            instance.save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("show {} {}".format(model.__name__, instance.id))
                output = f.getvalue().strip()
                self.assertIn(model.__name__, output)
                self.assertIn(instance.id, output)

    def test_destroy(self):
        """
        Test destroy command for each model
        """
        for model in self.models:
            instance = model()
            instance.save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("destroy {} {}".format(model.__name__, instance.id))
                self.assertNotIn("{}.{}".format(model.__name__, instance.id), storage.all().keys())

    def test_all(self):
        """
        Test all command for each model
        """
        for model in self.models:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("all {}".format(model.__name__))
                output = f.getvalue().strip()
                self.assertIsInstance(output, str)

    def test_update(self):
        """
        Test update command for each model
        """
        for model in self.models:
            instance = model()
            instance.save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd('update {} {} name "Test"'.format(model.__name__, instance.id))
                self.assertEqual(instance.name, "Test")

    def test_update_with_dict(self):
        """
        Test update command with dictionary for each model
        """
        for model in self.models:
            instance = model()
            instance.save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd('{}.update({}, {{"name": "Test", "age": 30}})'.format(model.__name__, instance.id))
                
                self.assertEqual(instance.name, "Test")

    def test_count(self):
        """
        Test <class name>.count() command for each model
        """
        for model in self.models:
            model()
            model().save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("{}.count()".format(model.__name__))
                count_output = f.getvalue().strip().split("\n")[-1]
                self.assertEqual(count_output, "2")

    def test_all_with_class(self):
        """
        Test <class name>.all() command for each model
        """
        for model in self.models:
            instance = model()
            instance.save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("{}.all()".format(model.__name__))
                output = f.getvalue().strip()
                self.assertIn(model.__name__, output)
                self.assertIn(instance.id, output)

    def test_show_with_onecmd(self):
        """
        Test <class name>.show(<id>) command for each model
        """
        for model in self.models:
            instance = model()
            instance.save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd('{}.show("{}")'.format(model.__name__, instance.id))
                output = f.getvalue().strip()
                self.assertIn(model.__name__, output)
                self.assertIn(instance.id, output)

    def test_destroy_with_onecmd(self):
        """
        Test <class name>.destroy(<id>) command for each model
        """
        for model in self.models:
            instance = model()
            instance.save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd('{}.destroy("{}")'.format(model.__name__, instance.id))
                self.assertNotIn("{}.{}".format(model.__name__, instance.id), storage.all().keys())

    def test_update_with_onecmd(self):
        """
        Test <class name>.update(<id>, <attribute name>, <attribute value>) command for each model
        """
        for model in self.models:
            instance = model()
            instance.save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd('{}.update("{}", "name", "Test")'.format(model.__name__, instance.id))
                self.assertEqual(instance.name, "Test")

    def test_update_with_dict_onecmd(self):
        """
        Test <class name>.update(<id>, <dictionary representation>) command for each model
        """
        for model in self.models:
            instance = model()
            instance.save()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd('{}.update({}, {{"name": "Test", "age": 30}})'.format(model.__name__, instance.id))
                self.assertEqual(instance.name, "Test")
                self.assertEqual(int(instance.age), 30)

if __name__ == '__main__':
    unittest.main()

