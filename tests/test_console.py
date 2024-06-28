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


class test_Console(unittest.TestCase):
    '''
    Test all features of the console: command and
    non-command line arguments.
    '''
    def setUp(self):
        """
        Setup before each test
        """
        self.console = HBNBCommand()

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

    def test_emptyline(self):
        """
        Test empty line input
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual("", f.getvalue().strip())

    def test_do_create(self):
        """
        Test create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.assertIn("User.{}".format(user_id), storage.all().keys())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create NonExistentClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_do_show(self):
        """
        Test show command
        """
        new_user = User()
        new_user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User {}".format(new_user.id))
            output = f.getvalue().strip()
            self.assertIn("User", output)
            self.assertIn(new_user.id, output)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show NonExistentClass {}".format(new_user.id))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User NonExistentID")
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_do_destroy(self):
        """
        Test destroy command
        """
        new_user = User()
        new_user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User {}".format(new_user.id))
            self.assertNotIn("User.{}".format(new_user.id), storage.all().keys())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy NonExistentClass {}".format(new_user.id))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User NonExistentID")
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_do_all(self):
        """
        Test all command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertIsInstance(output, str)

        new_user = User()
        new_user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            output = f.getvalue().strip()
            self.assertIn("User", output)
            self.assertIn(new_user.id, output)

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all NonExistentClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_do_update(self):
        """
        Test update command
        """
        new_user = User()
        new_user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('update User {} first_name "John"'.format(new_user.id))
            self.assertEqual("obj exist", f.getvalue().strip())
            self.assertEqual(new_user.first_name, "John")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User NonExistentID first_name John")
            self.assertEqual("** no instance found **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update NonExistentClass NonExistentID first_name John")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('update User {} first_name'.format(new_user.id))
            self.assertEqual("** value missing **", f.getvalue().strip())

    def test_update_with_dict(self):
        """
        Test update command with dictionary
        """
        new_user = User()
        new_user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('User.update("{}", {{"first_name": "John", "age": 30}})'.format(new_user.id))
            self.assertEqual(new_user.first_name, "John")
            self.assertEqual(new_user.age, 30)

    def test_count(self):
        """
        Test <class name>.count() command
        """
        new_user1 = User()
        new_user1.save()
        new_user2 = User()
        new_user2.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.count()")
            self.assertEqual(f.getvalue().strip(), "2")

    def test_all_with_class(self):
        """
        Test <class name>.all() command
        """
        new_user = User()
        new_user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.all()")
            output = f.getvalue().strip()
            self.assertIn("User", output)
            self.assertIn(new_user.id, output)

    def test_update_with_dict(self):
        """
        Test update command with dictionary
        """
        new_user = User()
        new_user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('User.update("{}", {{"first_name": "John", "age": 30}})'.format(new_user.id))
            self.assertEqual(new_user.first_name, "John")
            self.assertEqual(int(new_user.age), 30)

    def test_count(self):
        """
        Test <class name>.count() command
        """
        new_user1 = User()
        new_user1.save()
        new_user2 = User()
        new_user2.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.count()")
            count_output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(count_output, "2")

    def test_all_with_class(self):
        """
        Test <class name>.all() command
        """
        new_user = User()
        new_user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.all()")
            output = f.getvalue().strip()
            self.assertIn("User", output)
            self.assertIn(new_user.id, output)

    def test_show_with_onecmd(self):
        """
        Test <class name>.show(<id>) command
        """
        new_user = User()
        new_user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('User.show("{}")'.format(new_user.id))
            output = f.getvalue().strip()
            self.assertIn("User", output)
            self.assertIn(new_user.id, output)

    def test_destroy_with_onecmd(self):
        """
        Test <class name>.destroy(<id>) command
        """
        new_user = User()
        new_user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('User.destroy("{}")'.format(new_user.id))
            self.assertNotIn("User.{}".format(new_user.id), storage.all().keys())

    def test_update_with_onecmd(self):
        """
        Test <class name>.update(<id>, <attribute name>, <attribute value>) command
        """
        new_user = User()
        new_user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('User.update("{}", "first_name", "John")'.format(new_user.id))
            self.assertEqual(new_user.first_name, "John")

    def test_update_with_dict_onecmd(self):
        """
        Test <class name>.update(<id>, <dictionary representation>) command
        """
        new_user = User()
        new_user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('User.update("{}", {{"first_name": "John", "age": 30}})'.format(new_user.id))
            self.assertEqual(new_user.first_name, "John")
            self.assertEqual(int(new_user.age), 30)


if __name__ == '__main__':
    unittest.main()
