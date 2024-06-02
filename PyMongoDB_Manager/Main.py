import json
import pymongo
import time
import collection_handling as collection

client = pymongo.MongoClient('mongodb://localhost:27017/')


#Yeah yeah i know i alwasy use this but it took me an annoying while to figure out and i dont want to re do that
def display_options(title,options):
    print("\n")
    print("+-----------------------------------+")
    print(f"|          {title}")
    print("+-----------------------------------+")
    # For option in options do. The "i" is used because it counts up, enumerate enumerates the list starting from the number given (so it starts counting from 1 instead of 0).
    for i, option in enumerate(options, 1): 
        print(f"|  {i}. {option}") # if you ut the {} it will print a variable like text and again the f makes the string more fancy
    print("+-----------------------------------+")

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