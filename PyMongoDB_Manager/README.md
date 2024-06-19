PyMongoDB\_Manager
==================
****
Overview
--------

**PyMongoDB\_Manager** is a Python module designed to facilitate interaction with MongoDB databases. It provides a user-friendly interface to create databases, add information to existing databases, and interact with various collections within a MongoDB database. 

I made this for my personal use only but then decided to put it here on github because I thought it was interesting I know the functionality is heavily limited, but as I mentioned it wasn't intended for external users

Features
--------

*   Create new MongoDB databases.
    
*   Add information to existing databases.
    
*   Interact with collections to insert data.
    
*   Supports custom data structures for collections.
    

Installation
------------

To use **PyMongoDB\_Manager**, you need to have Python and MongoDB installed on your machine. Additionally, you'll need the pymongo library you can install pymongo using pip, finally run the Main.py file.

### 1\. Creating a New Database

You can create a new database and a collection by running the main script. The script will prompt you to enter the name of the new database and the initial collection.

### 2\. Adding Information to a Database

The script allows you to select an existing database and a collection to add information to. You can choose between using a predefined JSON structure or creating a new custom structure.

### 3\. Interacting with Collections

The collections class provides methods to interact with various collections within a MongoDB database. It includes methods for adding information to collections such as Profesores, Materias, and Calificaciones.
