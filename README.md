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
- [Ryan Apreala]
- [Jacqueline Tuyisenge]

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
