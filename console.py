#!/usr/bin/python3
"""console.py - entry point of the command interpreter"""
import cmd
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
        quit()
        return True

    do_EOF = do_quit
    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass
    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)"""
        if self.classes[args]:
            ob = self.classes[args]()
            print("{}".format(getattr(ob, 'id')))
            ob.save()
        elif not args:
            print("** class name missing **")
        elif  args not in self.classes:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the
        class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            k = args[0] + "." + args[1]
            ob = storage.all()
            if  ob.get(k):
                print(ob[k])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the
        change into the JSON file)"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            k = "BaseModel"+ "." + args[1]
            ob = storage.all()
            if ob.get(k):
                del ob[k]
                storage.save()
            else:
                print("** no instance found **")
    def do_all(self, arg):
        """func do_all - arg - Prints all string representation of all
         instances based or not on the class name"""
        a = storage.all()
        if arg in self.classes:
            print(a)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
         updating attribute"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            if args[0] in self.classes:
                k = args[0] + "." + args[1]
                ob = storage.all().get(k)
                if k in ob:
                    ob.__setattr__(args[2], type(ob.__getattr__(args[2]))(args[3]))
                    ob[k].update_at = datetime.now()
                    storage.save()
                else:
                    print("** no instance found **")
            
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()
