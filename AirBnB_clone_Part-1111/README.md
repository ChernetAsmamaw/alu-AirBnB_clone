# AirBnB clone - The console

The console is the first part of the **AirBnB clone** project which aims to deploy a simple copy of the AirBnB website to cover all fundamental concepts of the Holberton School higher level programming track.

<br>

<div align=center>  
    <img  
    style="text-align:center"  
    src="https://raw.githubusercontent.com/ChernetAsmamaw/hbtn_config/main/assets/hbnb.png"  
    alt="holbertonbnb"/>  
</div>

<br>

## Overview

This first part of the project focuses on creating a command interpreter that allows to:

- create the data model.
- manage (create, update and destroy) objects via a console.
- store and persist objects to a file (JSON file).

## Files and Directories

**`/models`** directory constains all classes used for the project.  
[basemodel.py](https://github.com/ChernetAsmamaw/AirBnB_clone/blob/main/models/base_model.py) file contains the base class (**BaseModel**) of all models in the project:

- [user.py](https://github.com/ChernetAsmamaw/AirBnB_clone/blob/main/models/user.py) - file contains the `User` class.
- [state.py](https://github.com/ChernetAsmamaw/AirBnB_clone/blob/main/models/state.py) - file contains the `State` class.
- [city.py](https://github.com/ChernetAsmamaw/AirBnB_clone/blob/main/models/city.py) - file contains the `City`class.
- [amenity.py](https://github.com/ChernetAsmamaw/AirBnB_clone/blob/main/models/amenity.py) - file contains the `Amenity` class.
- [place.py](https://github.com/ChernetAsmamaw/AirBnB_clone/blob/main/models/place.py) - file contains the `Place` class.
- [review.py](https://github.com/ChernetAsmamaw/AirBnB_clone/blob/main/models/review.py) - file contains the `Review` class.

**`/models/engine`** directory contains the class that handles JASON serialization and deserialization.  
[file_storage.py](https://github.com/ChernetAsmamaw/AirBnB_clone/blob/main/models/engine/file_storage.py) - file contains `FileStorage` class.

**`/tests`** directory contains all unit test cases for this project.

[console.py](https://github.com/coding-max/AirBnB_clone/blob/main/console.py) the console contains the entry point of the command interpreter.

<br>

```
|── console.py
├── models/
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   |── user.py
│   └── engine/
│       └── file_storage.py
└── tests/
    |── test_console.py
    └── test_models/
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        |── test_user.py
        └── test_engine/
            └── test_file_storage.py
```

## Environment and Execution

This project was interpreted/compiled and tested on Ubuntu 14.04 LTS using python3 (version 3.4.3).

To use the console you must have `pyhton3` installed and the repository cloned  
(`git clone git@github.com:ChernetAsmamaw/AirBnB_clone.git`).

To start the console you only need to run `./console` in the root of the repository.

The console works like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb)
(hbnb) create BaseModel
bc0474a9-54b3-435b-a872-d77dc2a45b09
(hbnb) create User
dc8e6fbe-4370-4740-86c3-e6de3e566953
(hbnb) count BaseModel
1
(hbnb) destroy BaseModel bc0474a9-54b3-435b-a872-d77dc2a45b09
(hbnb) count BaseModel
0
(hbnb)
(hbnb)
(hbnb) quit
$

```

## Authors

    Part-1

- [Chernet Asmamaw](https://www.linkedin.com/in/chernet-asmamaw-34a421241/)
- [Bevil Mulor](https://www.linkedin.com/in/bevil-mulor-726b13260?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BZKogAbCdSFa9k7L2q2I5uA%3D%3D)
