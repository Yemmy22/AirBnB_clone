#!/usr/bin/python3
'''
HBNB class module.
'''

import cmd


class HBNBCommand(cmd.Cmd):
    '''
    A subclass of the Cmd class with defined commands.
    '''
    
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
