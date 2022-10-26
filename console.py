#!/usr/bin/python3
"""This module is the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for command interpreter"""
    prompt = '(hbnb) '
    classDict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_quit(self, arg):
        """Quit command to return quit program function"""
        return True

    def do_EOF(self, arg):
        """EOF command to return exit program function"""
        return True

    def emptyline(self):
        """Empty line handeler"""
        return False

    def do_create(self, arg):
        """create a new intance of basemodel"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in self.classDict:
            newEl = self.classDict.get(args[0])()
            storage.save()
            print(newEl.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string repr of an instance based on id and cls name"""
        args = arg.split()
        classDict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classDict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif F"{args[0]}.{args[1]}" not in classDict:
            print("** no instance found **")
        else:
            print(classDict[F"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        """Deletes an instance based on class name & id"""
        args = arg.split()
        classDict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classDict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif F"{args[0]}.{args[1]}" not in classDict:
            print("** no instance found **")
        else:
            del classDict[F"{args[0]}.{args[1]}"]
            storage.save()

    def do_all(self, arg):
        """Prints all str repr of all instances based or not on the cls name"""
        args = arg.split()
        classDict = storage.all()
        if len(args) == 0:
            for el in classDict:
                print(classDict[el])
        if len(args) == 1:
            if args[0] in self.classDict:
                for key, value in classDict.items():
                    if value.__class__.__name__ == args[0]:
                        print(value)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """update"""
        args = arg.split()
        classDict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classDict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                setattr(storage.all()[key], args[2], args[3])
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
