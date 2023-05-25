<<<<<<< HEAD
#!/usr/bin/python3
"""Class State that inherits from the BaseModel class"""

from models import BaseModel


class State(BaseModel):
    """State class"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
=======
#!/usr/bin/python3

from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel"""
    name = ""
>>>>>>> cc1bd00f1ca76611591882c0c790a7e0e53b17b7
