#!/usr/bin/python3

from uuid import uuid4 as u4
from datetime import datetime
from models import storage


class BaseModel:

    def __init__(self, *args, **kwargs):
        # Here we're checking if kwargs is empty or not. 
        # Wether it is empty or not we are going to create a new instance of 
        #   the class with the id and the created_at and updated_at attributes.
        # We can also check if it's empty by doing 
        #           if not kwargs: or if kwargs == {}: or if kwargs is None:
        if kwargs:
            for key, value in kwargs.items():
                # Here we are checking if the key is equal to the class name, 
                #   if it is we are going to skip it.
                # This is because we don't want to set the class name as an attribute.
                # Each key of the dictionary is an attribute name and each value of the
                #    dictionary is the value of the attribute name.
                if key == '__class__':
                    continue
                # Here we are checking if the key is equal to the created_at or updated_at,
                #    if it is we are going to convert the string to a datetime object.
                elif key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                # If all the above conditions are not met, we are going to set the key 
                #   and value as an attribute.
                else:
                    self.__dict__[key] = value
        else:
            # Public instance attributes: id, created_at, updated_at
            # These are assigned when an instance is created 
            self.id = str(u4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    
    # __str__: should print: [<class name>] (<self.id>) <self.__dict__>
    def __str__(self):
        string = "[{}] ({}) {}" .format(
            self.__class__.__name__, self.id, self.__dict__)
        return string
    
    
    # Public instance methods: save, to_dict
    # save: updates updated_at with the current datetime
    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    # to_dict: returns a dictionary of all keys/values of __dict__ of the instance
    def to_dict(self):  
        # copy of the dictionary of the instance so we don’t modify the original
        # The data is also different as it's converted to string and in ISO format
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        # created_at & updated_at: change from datetime object to string(ISO format)
        # Here instead of creating new variables we can also use: 
        #           old_created = self.created_at and old_updated = self.updated_at

        old_created = new_dict["created_at"]
        old_updated = new_dict["updated_at"]
        created = old_created.isoformat()
        updated = old_updated.isoformat()
        new_dict["created_at"] = created
        new_dict["updated_at"] = updated
        return new_dict
