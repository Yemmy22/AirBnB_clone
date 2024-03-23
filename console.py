#!/usr/bin/python3
'''
HBNB class module.
'''

import cmd
from models.base_model import BaseModel
from models.user import User
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    '''
    A subclass of the Cmd class with defined commands.
    '''

    prompt = '(hbnb) '
    class_list = ["BaseModel", "User", "Fake"]

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print('Quit command to exit the program\n')

    def do_quit(self, line):
        return True

    def help_quit(self):
        print('Quit command to exit the program\n')

    def emptyline(self):
        return

    def do_create(self, line):
        """Create an instance of a specified class"""
        if line:
            if line in self.class_list:
                new_obj = eval(line)()
                new_obj.save()
                print(new_obj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Display the string representation of an instance"""
        if line:
            args = line.split()
            if len(args) <= 2:
                if args[0] not in self.class_list:
                    print("** class doesn't exist **")
                else:
                    if len(args) == 1:
                        print("** instance id missing **")
                    else:
                        all_obj = storage.all()
                        for obj_key in all_obj:
                            key = "{}.{}".format(args[0], args[1])
                            if key == obj_key:
                                print(all_obj[obj_key])
                                return
                        print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Delete an instance based on the class name and id"""
        if line:
            args = line.split()
            if len(args) <= 2:
                if args[0] not in self.class_list:
                    print("** class doesn't exist **")
                else:
                    if len(args) == 1:
                        print("** instance id missing **")
                    else:
                        all_obj = storage.all()

                        for obj_key, obj in storage.all().items():
                            key = "{}.{}".format(args[0], args[1])
                            if key == obj_key:
                                del(all_obj[key])
                                storage.save()
                                return
                        print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Display string representations of all instances"""
        obj_list = []
        if line:
            for obj in storage.all().values():
                if obj.__class__.__name__ == line:
                    obj_list.append(str(obj))
            if not obj_list:
                print("** class doesn't exist **")
                return
        else:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, line):
        """Update an instance attribute"""
        if line:
            arg = line.split(' ')
            if arg[0] not in self.class_list:
                print("** class doesn't exist **")
            else:
                if len(arg) == 1:
                    print("** instance id missing **")
                elif len(arg) == 2:
                    obj_copy = False
                    for obj in storage.all().values():
                        if arg[1] == obj.id:
                            obj_copy = True
                    if obj_copy is True:
                        print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                elif len(arg) == 3:
                    print("** value missing **")
                else:
                    const_attr = ["id", "created_at", "updated_at"]
                    if arg[2] not in const_attr:

                        all_obj = storage.all()
                        for obj_key, obj in all_obj.items():
                            key = "{}.{}".format(arg[0], arg[1])
                            if key == obj_key:
                                attr = arg[2]
                                attr_type = type(arg[2])
                                attr_value = arg[3].strip('"').strip("'")
                                setattr(obj, attr, attr_type(attr_value))
                                obj.save()
                                return
                        print("** no instance found **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
