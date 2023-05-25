#!/usr/bin/python3
<<<<<<< HEAD
"""Class representing a user"""
from models.base_model import BaseModel


class User(BaseModel):
    """Details of a user"""
=======

from models.base_model import BaseModel

# User has public class attributes email, password, first_name, last_name
class User(BaseModel):
    """User class that inherits from BaseModel"""
>>>>>>> cc1bd00f1ca76611591882c0c790a7e0e53b17b7
    email = ""
    password = ""
    first_name = ""
    last_name = ""

<<<<<<< HEAD
    """def __init__(self, *args, **kwargs):
        Initialize a User instance
        super().__init__(*args, **kwargs)"""
=======
>>>>>>> cc1bd00f1ca76611591882c0c790a7e0e53b17b7
