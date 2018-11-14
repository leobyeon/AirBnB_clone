#!/usr/bin/python3
"""console.py - entry point of the command interpreter"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand - func """
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file)
        """
        if self.classes.get(args):
            ob = self.classes[args]()
            print("{}".format(getattr(ob, 'id')))
            ob.save()
        elif not args:
            print("** class name missing **")
        elif args not in self.classes:
            print("** class doesn't exist **")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            k = args[0] + "." + args[1]
            ob = storage.all()
            if ob.get(k):
                print(ob[k])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the
        change into the JSON file)
        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            k = args[0] + "." + args[1]
            ob = storage.all()
            if ob.get(k):
                del ob[k]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        func do_all - arg - Prints all string representation of all
        instances based or not on the class name
        """
        a = storage.all()
        a_list = []
        if not arg:
            for v in a.values():
                a_list.append(str(v))
            print(a_list)
        else:
            if arg in self.classes:
                for k, v in a.items():
                    splitkey = k.split(".")
                    if splitkey[0] == arg:
                        a_list.append(str(v))
                print(a_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            if storage.all().get(args[0] + "." + args[1]):
                print("** attribute name missing **")
            else:
                print("** no instance found **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            if args[0] in self.classes:
                k = args[0] + "." + args[1]
                ob = storage.all()
                if k in ob:
                    obj = ob.get(k)
                    try:
                        attr = getattr(obj, args[2])
                        setattr(obj, args[2], type(attr)(args[3]))
                    except:
                        setattr(obj, args[2], args[3])
                    storage.save()
                else:
                    print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
