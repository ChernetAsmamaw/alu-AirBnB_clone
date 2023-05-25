<<<<<<< HEAD
![hBnB](https://BevilMulor/alu-AirBnB_clone/blob/main/images/hbnb.png?raw=true)

# alu-AirBnB_clone
# AirBnB Clone Command Interpreter

## Project Description
The AirBnB Clone Command Interpreter is a Python-based project that implements a command line interface for managing AirBnB objects. It allows users to create, retrieve, update, and delete objects such as Users, States, Cities, and Places. The project utilizes serialization and deserialization techniques, file storage, and unit testing to ensure the functionality and correctness of the implemented classes and features.

## Command Interpreter Usage

### Starting the Command Interpreter
To start the AirBnB Clone Command Interpreter, follow these steps:

1. Clone the project repository from GitHub.
2. Navigate to the project directory
3. Open a terminal or command prompt in the project directory.

### Launching the Command Interpreter
To launch the command interpreter, execute the following command:

**$ ./console.py**

After executing the command, you will enter the command prompt for the AirBnB Clone Command Interpreter.

### Using the Command Interpreter
The command interpreter supports various commands for managing AirBnB objects. Here are some examples of the available commands:

- `create <class_name>`: Create a new instance of the specified class.
- `show <class_name> <object_id>`: Display the details of a specific object.
- `all` or `all <class_name>`: Display all objects or objects of a specific class.
- `update <class_name> <object_id> <attribute_name> "<attribute_value>"`: Update the value of a specific attribute of an object.
- `destroy <class_name> <object_id>`: Delete a specific object.
- `count <class_name>`: Count the number of objects of a specific class.

You can also type `help` to see the list of available commands and their descriptions.

### Examples
Here are some examples of how to use the AirBnB Clone Command Interpreter:

- Creating a new User object: _**(hbnb) create User**_
- Updating the name attribute of a Place object: _**(hbnb) update Place <place_id> name "New Place Name"**_
- Displaying all City objects: _**(hbnb) all City**_
- Deleting a specific object: **_(hbnb) destroy User <user_id>_**

## Unit Testing
The project includes unit tests to verify the functionality and accuracy of the implemented classes and features. The tests are organized in the `tests` directory and can be executed using the following command:

_**$ python3 -m unittest discover tests**_

Running the command will execute all the unit tests and display the results.

## Requirements
- Python 3.8.5 or higher
- pycodestyle 2.7.* (for code style checking)

## Authors
- [Bevil Mulor]
- [Chernet Asmamaw]
=======
# AirBnB Clone - The Complete Project

The goal of this project is deploy on server a simple copy of the AirBnB website to cover all fundamental concepts of the higher level programming track of ALU BSE Course.

<div align=center>  
    <img  
    style="text-align:center"  
    src="https://github.com/ChernetAsmamaw/alu-AirBnB_clone/blob/main/assets/airbnb_clone.png"
    alt="ALU BSE"/>  
</div>

## Description

The complete web application will be composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell.
- A website (the front-end) that shows the final product to everybody: static and dynamic.
- A database or files that store data.
- An API that provides a communication interface between the front-end and the data (retrieve, create, delete and update).

## Stages

| Stage         | Repo                                                                      |
| ------------- | ------------------------------------------------------------------------- |
| The console   | [AirBnB_clone_Part-1](https://github.com/ChernetAsmamaw/alu-AirBnB_clone) |
| Web static    | :soon:                                                                    |
| MySQL storage | :soon:                                                                    |
| Web framework | :soon:                                                                    |
| RESTful API   | :soon:                                                                    |
| Web dynamic   | :soon:                                                                    |

### Infrastructure diagram

<div align=center>  
    <img  
    style="text-align:center"  
    src="https://github.com/ChernetAsmamaw/alu-airbnb_clone/blob/main/assets/infrastructure_diagram.png"   
    alt="infrastructure diagram"/>  
</div>
...

...

...

...

...

...

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
>>>>>>> cc1bd00f1ca76611591882c0c790a7e0e53b17b7
