<<<<<<< HEAD
#!/usr/bin/python3
"""Class Review that inherits from the BaseModel class"""

from models import BaseModel


class Review(BaseModel):
    """Review class"""

    place_id = ""  # string - empty string: it will be the Place.id
    user_id = ""  # string - empty string: it will be the User.id
    text = ""  # string - empty string

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
=======
#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
>>>>>>> cc1bd00f1ca76611591882c0c790a7e0e53b17b7
