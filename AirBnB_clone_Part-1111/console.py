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
        # If the arg is class name then we create an instance of that class & save it
        else:
            from models.base_model import BaseModel
            from models.user import User
            from models.place import Place
            from models.city import City
            from models.state import State
            from models.amenity import Amenity
            from models.review import Review
            
            # Same as new_instance = BaseModel() but dynamically checking for the class  
            # we are using eval() so that we get a class type and not a string
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the 
        class name and id respectively.
        Usage: show <class name> <id>
        Example: show BaseModel 1234-1234-1234 """
        
        # The argument is passed as a string, we split it into a list for easy access
        arg_list = args.split()
        #print(arg_list)
        
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

        #elif "{}.{}".format(arg_list[0], arg_list[1]) not in storage.all():
            #print("** no instance found **")
        #else:
            #print(storage.all()["{}.{}".format(arg_list[0], arg_list[1])])
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
            # Because the key is split above, we concatenate the two strings to get a key
            # The key that retrieves the object information form the JSON file
            else:
                key = "{}.{}".format(arg_list[0], arg_list[1])
                info = obj_list[key]
                print(info)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id respectively
        then save the change into the JSON file.
        Usage: destroy BaseModel 1234-1234-1234 """

        # The argument is passed as a string, we split it into a list for easy access
        arg_list = args.split()
        #print(arg_list)
        
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
        # The storage object is a dictionary of objects created by the FileStorage class
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
        """Updates an instance based on the class name and id respectively
        by adding or updating attribute then save the change into the JSON file.
        Usage:  update <class name> <id> <attribute name> "<attribute value>
                Example: - update BaseModel 1234-1234-1234 email "aibnb@mail.com\""""


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
        # This is to handle the case when the user enters <class name>.<command> 
        # For example:  City.all() User.show(<id>) or Place.destroy(<id>) or 
        #               State.update(<id>, <attribute name>, <attribute value>)
        

        if "." in line:
            if "()" in line:
                # Handle the case when the command has no arguments
                line = line.replace(".", " ").replace("(", "").replace(")", "")
                # Here we created a tuple of the command that we want to execute
                line = line.split(" ")
                line = str(line[1]) + " " + str(line[0])
            elif "(" in line and ")" in line:
                line = line.replace(".", " ").replace("(", " ").replace(")", "")
                # Here we created a tuple of the command that we want to execute
                line = line.split(" ")
                if len(line) == 3:
                    # This removes the double quotes from the string
                    line[2] = line[2].replace('"', '')
                    line = str(line[1]) + " " + str(line[0]) + " " + str(line[2])
                
                elif len(line) == 4:
                    line[2] = line[2].replace('"', '')
                    print(line)
                    line[3] = line[3].replace('"', '')
                    print(line)
                    line = str(line[1]) + " " + str(line[0]) + " " + str(line[2]) + " " + str(line[3])
                    print(line)
            
            

            else:
                pass      
        
        
        return cmd.Cmd.precmd(self, line)









    

# This makes the codes in this file to not execute when imported 
# only excute when run as a separate file
# The cmdloop() method is used to start the interpreter loop
if __name__ == '__main__':
    HBNBCommand().cmdloop("\n Hello! Welcome to the Matrix.\n")
