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

def not_added():
    print("This function is yet to be added")

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


def add_info(db_list):
    """
    Course of actions after choosing the 2nd option in the main menu
    Display option to select a Database (db) and afterwards a collection (cll) inside said db
    After selecting the collection the user is prompted to choose an action to execute on that collection

    Args:
        db_list (list): The list of DataBases present.

    Returns:
        None
    """

    #1st Options Menu
    display_options("Choose DataBase          |",db_list)

    db_use = input("--> ")
    collection_instance = collection.collections(db_use)

    db = client[db_use]

    
    # 2nd Options Menu
    collection_names = db.list_collection_names()
    cll_list = []
    for name in collection_names:
        cll_list.append(name)

    display_options("Choose Collection        |",cll_list)

    cll_use = input("--> ")

    #3rd option menu

    wtd = ["Use Premade JSON Structure    |","Make New JSON Structure       |"]
    display_options("What To do?              |",wtd)

    do = input("--> ")

    if do == "1":
        collection_instance.execute_function(cll_use)
    elif do == "2":
        collection_instance.new_structure(cll_use)
    else:
        print("Invalid Option. Choose Between 1 or 2")
    


# Main function to display the menu and handle user input.
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
        add_info(database_list)



if __name__ == "__main__":
    main()