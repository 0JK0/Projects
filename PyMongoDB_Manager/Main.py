"""
Main Module for PyMongoDB Manager, This script Provivdes functionalities to
- Create new Mongodb Data Bases
- Add informaton to existing Data Bases
- Interact with collections
"""

# Working on a rework for this since i found this interesting

import json
import pymongo
import time
import collection_handling as collection

# Establish a connection to the MongoDB server
client = pymongo.MongoClient('mongodb://localhost:27017/') 

def display_options(title,options):
    """
    Displays a formatted list of options with a title.

    Args:
        title (str): The title of the options menu.
        options (list): A list of options to display.
    """
        
    print("\n")
    print("+-----------------------------------+")
    print(f"|          {title}")
    print("+-----------------------------------+")

    for i, option in enumerate(options, 1): 
        print(f"|  {i}. {option}") 
    print("+-----------------------------------+")


# Creates a new database and a collection in MongoDB based on user input.
def create_database():
    client = pymongo.MongoClient('mongodb://localhost:27017/')

    existing_database = client.list_database_names()

    new_database_name = input("Enter the name for the new DataBase: ")
    collection_name = input("Enter the name for the 1st collection: ")

    db = client[new_database_name]
    
    try:
        db.create_collection(collection_name)
        print("Database and Collection created successfully!")
    except Exception as e:
        print("Error: ", e)


# Main function to display the menu and hanlde user input.
def main():

    main_menu = ["Make New DataBase             | ","Add Info to Data Base         |"]
    display_options("PyMongoDB Manager        |",main_menu)

    start = input("--> ")
    
    database_names = client.list_database_names()
    database_list = []
    for name in database_names:
        database_list.append(name)

    if start == "1":
        create_database()

    elif start == "2":

        display_options("Choose DataBase          |",database_list)

        db_use = input("--> ")
        collection_instance = collection.collections(db_use)

        db = client[db_use]

        

        collection_names = db.list_collection_names()
        collection_list = []
        for name in collection_names:
            collection_list.append(name)

        display_options("Choose Collection        |",collection_list)

        user_input = input("--> ")

        collection_instance.execute_function(user_input)



if __name__ == "__main__":
    main()