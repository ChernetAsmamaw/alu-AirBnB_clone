<<<<<<< HEAD
#!/usr/bin/python3
"""Class City that inherits from the BaseModel class"""

from models import BaseModel


class City(BaseModel):
    """City class"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
=======
#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel"""
    state_id = ""
    name = ""
>>>>>>> cc1bd00f1ca76611591882c0c790a7e0e53b17b7
