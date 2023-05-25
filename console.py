<<<<<<< HEAD
#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def default(self, line):
        """Catch commands if nothing else matches then."""
        # print("DEF:::", line)
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True

    def do_quit(self, line):
        """Exits the program.
        """
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass

    def do_create(self, line):
        """Creates an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """Prints the string representation of an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                line_str = [str(obj) for key, obj in storage.all().items()
                            if type(obj).__name__ == words[0]]
                print(line_str)
        else:
            line_str = [str(obj) for key, obj in storage.all().items()]
            print(line_str)

    def do_count(self, line):
        """Counts the instances of a class.
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def do_update(self, line):
        """Updates an instance by adding or updating attribute.
        """
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
=======
#!/usr/bin/python3

import cmd
from models import storage

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
    """Command line interpreter for AirBnB project"""
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
        Example: show BaseModel 1234-1234-1234 """

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
        Usage: destroy BaseModel 1234-1234-1234 """

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

    def precmd(self, line):
        # Precmd a cmd method that is called before the command is executed
        # This handels the case when the user enters <class name>.<command>
        # For example:  City.all() User.show(<id>) or Place.destroy(<id>) or
        #               State.update(<id>, <attribute name>, <attribute value>)

        if "." in line:
            if "()" in line:
                # Handle the case when the command has no arguments
                line = line.replace(".", " ").replace("(", "").replace(")", "")
                # Here we created a tuple of the command to be executed
                line = line.split(" ")
                line = str(line[1]) + " " + str(line[0])
            elif "(" in line and ")" in line:
                line = line.replace(".", " ").replace(
                    "(", " ").replace(")", "")
                # Here we created a tuple of the command to be excuted
                line = line.split(" ")
                if len(line) == 3:
                    # This removes the double quotes from the string
                    line[2] = line[2].replace('"', '')
                    line = str(line[1]) + " " + \
                        str(line[0]) + " " + str(line[2])
                elif len(line) == 4:
                    line[2] = line[2].replace('"', '')
                    print(line)
                    line[3] = line[3].replace('"', '')
                    print(line)
                    line = str(line[1]) + " " + str(line[0]) + \
                        " " + str(line[2]) + " " + str(line[3])
                    print(line)

            else:
                pass

        return cmd.Cmd.precmd(self, line)

    # This makes the codes in this file to not execute when imported
    # only excute when run as a separate file
    # The cmdloop() method is used to start the interpreter loop
if __name__ == '__main__':
    HBNBCommand().cmdloop("\n Hello! Welcome to the Matrix.\n")
>>>>>>> cc1bd00f1ca76611591882c0c790a7e0e53b17b7
