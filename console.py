#!/usr/bin/python3
'''
HBNB class module.
'''

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    '''
    A subclass of the Cmd class with defined commands.
    '''

    prompt = '(hbnb) '
    class_list = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            ]

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
        """
        Create an instance of a specified class
        """
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
        """
        Display the string representation of an instance
        """
        if line:
            args = line.split()
            if len(args) <= 2:
                if args[0] not in self.class_list:
                    print("** class doesn't exist **")
                else:
                    if len(args) < 2:
                        print("** instance id missing **")
                    else:
                        all_obj = storage.all()
                        for obj_key in all_obj.keys():
                            key = "{}.{}".format(args[0], args[1])
                            if key == obj_key:
                                print(all_obj[obj_key])
                                return
                        print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
        Usage: destroy <class name> <id>
        Delete an instance based on the
        class name and id
        """
        if line:
            args = line.split()
            if args[0] not in self.class_list:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                elif len(args) == 2:
                    all_obj = storage.all()
                    for obj_key in all_obj:
                        key = "{}.{}".\
                            format(args[0], args[1])
                        if key == obj_key:
                            del (all_obj[key])
                            storage.save()
                            return
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        Display string representations of all instances
        """
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
        """
        Update an instance attribute
        """
        if line:
            arg = line.split(' ')
            if arg[0] not in self.class_list:
                print("** class doesn't exist **")
            else:
                if len(arg) < 2:
                    print("** instance id missing **")
                else:
                    obj_copy = False
                    for obj in storage.all().values():
                        if arg[1] == obj.id:
                            obj_copy = True
                    if not obj_copy:
                        print("** no instance found **")
                    else:
                        if len(arg) < 3:
                            print("** attribute name missing **")
                        elif len(arg) < 4:
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
                                        attr_val = arg[3].strip('"').strip("'")
                                        setattr(obj, attr, attr_type(attr_val))
                                        obj.save()
                                        return
                                    print("** no instance found **")
        else:
            print("** class name missing **")

    def default(self, line):
        '''
        Mutes the error feedback.
        '''
        pass

    def onecmd(self, line):
        '''
        Processes Non-commands.
        '''
        arg = line.split('.')

        try:
            cmnd, data = arg[1].split('(')
            obj_id = data[:-1]
            obj_id = obj_id.strip('"')

            # Usage: <class name>.show(<id>)
            # Print all existing instances of the specified class

            if arg[0] in self.class_list and cmnd == "show":
                line = "show {} {}".format(arg[0], obj_id)

            # Usage: <class name>.destroy(<id>)
            # Delete a specified class instance.

            elif arg[0] in self.class_list and cmnd == "destroy":
                line = "destroy {} {}".format(arg[0], obj_id)

        except Exception:
            pass

            # Alternative code for <class name>.show(<id>):
            # elif arg[1].startswith("show("):
            # instance_id = arg[1][5:-1].strip('"')
            # line = f"show {arg[0]} {instance_id}"

        if len(arg) == 2:

            # Usage: <class name>.all()
            # Print all existing instances.
            if arg[0] in self.class_list and arg[1] == "all()":
                line = "all " + arg[0]

            # Usage: <class name>.count()
            # Print the total number of specified class

            if arg[0] in self.class_list and arg[1] == "count()":
                print(arg[0], arg[1])
                count = 0
                for key in storage.all():
                    obj_name, obj_id = key.split('.')
                    if obj_name == arg[0]:
                        count += 1
                print(count)
        return cmd.Cmd.onecmd(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
