#!/usr/bin/python3
"""Defines the HBnB console."""

import cmd
from models import storage

# This is a list of all the classes that we have created
list_of_classes = [
    "BaseModel",
    "User",
    "State",
    "City",
    "Amenity",
    "Place",
    "Review"
]


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for AirBnB project
    that can be used to manage the objects of our project"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Exits the program"""
        print("\nGoodbye!")
        return True
    # EOF(End Of File) is CTRl + D

    def do_EOF(self, args):
        """Exits the program  using CTRL + D"""
        # so that it doesn't continue on the same line
        print()
        return True

    # Overides the behavior to run privious command when pressed enter
    def emptyline(self):
        """Doesn't execute anything when enter is pressed"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, User or other classes...,
        saves it (to the JSON file) and prints the id.
        Usage: create <class name>
        Example: create BaseModel"""
        # If nothing is entered
        if len(args) == 0:
            print('** class name missing **')
        # If the argument being passed is not BaseModel
        elif args not in list_of_classes:
            print("** class doesn\'t exist **'")
        # If the arg is class name then we create an instance of that class
        else:
            from models.base_model import BaseModel
            from models.user import User
            from models.place import Place
            from models.city import City
            from models.state import State
            from models.amenity import Amenity
            from models.review import Review

            # Here we are dynamically creating a new instance of a class
            # we are using eval() so that we get a class type and not a string
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the
        class name and id respectively.
        Usage: show <class name> <id>
        Example: show BaseModel 1234-1234-1234"""

        # Argument is passed as a string, we split it into list for easy access
        arg_list = args.split()
        # print(arg_list)

        # If nothing is entered
        if len(arg_list) == 0:
            print('** class name missing **')
        # If the argument being passed is not BaseModel
        elif arg_list[0] not in list_of_classes:
            print("** class doesn\'t exist **'")
        # If the id is not passed
        elif len(arg_list) < 2:
            print('** instance id missing **')
        # We can write the code below in much shoter way: -
        # Sice the basic consept is that storage.all()[key] returns the
        # information of an object key being <class name>.<id>
        # elif "{}.{}".format(arg_list[0], arg_list[1]) not in storage.all():
            # print("** no instance found **")
        # else:
            # print(storage.all()["{}.{}".format(arg_list[0], arg_list[1])])
        # we have used this below in the destroy method
        else:
            # Here we check if the id entered exists in the JSON file
            obj_list = storage.all()
            id_list = []
            for key in obj_list.keys():
                id = key.split('.')[1]
                id_list.append(id)
            if arg_list[1] not in id_list:
                print("** no instance found **")
            # Because key is split we concatenate the two strings to get a key
            # The key that retrieves the object information form the JSON file
            else:
                key = "{}.{}".format(arg_list[0], arg_list[1])
                info = obj_list[key]
                print(info)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id respectively
        then save the change into the JSON file.
        Usage: destroy BaseModel 1234-1234-1234"""

        # Argument is passed as a string, we split it into list for easy access
        arg_list = args.split()
        # print(arg_list)

        # If nothing is entered
        if len(arg_list) == 0:
            print('** class name missing **')
        # If the argument being passed is not BaseModel
        elif arg_list[0] not in list_of_classes:
            print("** class doesn\'t exist **'")
        # If the id is not passed
        elif len(arg_list) < 2:
            print('** instance id missing **')
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()["{}.{}".format(arg_list[0], arg_list[1])]
            # SO that the deletion is saved in the JSON file
            storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances based on the class name.
        or not based on the class name.
        Usage: all BaseModel or all"""
        obj_list = []
        # If there are no arguments passed after the self parameter the loop
        # iterates over all the values in the storage object
        # And appends a string representation of each object to the obj_list.
        # Storage object is a dict of objects created by FileStorage class
        if len(args) == 0:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        # This checks if the argument passed is not BaseModel
        # If it isn't then it prints the message
        # After that it does the same thing as above(prints all the objects)
        else:
            if args not in list_of_classes:
                print("** class doesn\'t exist **'")
                return
            for key, value in storage.all().items():
                # The purpose of spliting the key is to get the class name and
                #  compare it with the argument passed
                class_name = key.split('.')[0]
                if class_name == args:
                    obj_list.append(str(value))
        print(obj_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute then save the change into the JSON file.
        Usage:  update <class name> <id> <attribute name> "<attribute value>
        Example: update BaseModel 1234-1234-1234 email "aibnb@mail.com\""""

        arg_list = args.split()
        if len(arg_list) == 0:
            print('** class name missing **')
        elif arg_list[0] not in list_of_classes:
            print("** class doesn\'t exist **'")
        elif len(arg_list) < 2:
            print('** instance id missing **')
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in storage.all():
            print("** no instance found **")
        elif len(arg_list) < 3:
            print('** attribute name missing **')
        elif len(arg_list) < 4:
            print('** value missing **')
        else:
            class_name = arg_list[0]
            id = arg_list[1]
            key = arg_list[2]
            value = arg_list[3]

            obj_key = class_name + "." + id
            obj = storage.all()[obj_key]
            obj.__dict__[key] = eval(value)
            storage.save()

    def do_count(self, args):
        """Retrieves the number of instances of a class.
        Usage: count <class name>"""

        count = 0
        for key in storage.all().keys():
            class_name = key.split('.')[0]
            if class_name == args:
                count += 1
        print(count)
        
    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False


# This makes the codes in this file to not execute when imported
# only excute when run as a separate file
# The cmdloop() method is used to start the interpreter loop
if __name__ == '__main__':
    HBNBCommand().cmdloop()
