import sqlite3
import os
import Routines
from datetime import date

def make_table():
    conn = sqlite3.connect("Tracking.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS routines (id INTEGER PRIMARY KEY,name TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY,name TEXT,date TEXT)")
    conn.commit()
    conn.close()

def show_table(table):
    conn = sqlite3.connect("Tracking.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table}")
    rows = c.fetchall()
    conn.close()
    return rows

def get_routine_name(id):
    from sqlite3 import Error

    try:
        conn = sqlite3.connect("Tracking.db")
        c = conn.cursor()

        c.execute(f"SELECT name FROM routines WHERE id = {id}")
        routine_record = c.fetchone()

        conn.commit()
        conn.close()

        routine_name = routine_record[0] if routine_record else None
        return routine_name
        
    except Error as e:
        print(f"Oops! Something went wrong. Error: {e}")
        # reverse the change in case of error
        conn.rollback()
        return None


def delete_data(id):
    from sqlite3 import Error

    try:
        conn = sqlite3.connect("Tracking.db")
        c = conn.cursor()

        sql_del = c.execute(f"DELETE FROM routines WHERE id = {id}")
        print(f"successfully deleted the routine number {id} ")

        conn.commit()
        conn.close()
    except Error as e:
        print(f"Oops! Something went wrong. Error: {e}")
        # reverse the change in case of error
        conn.rollback()


def insert(table,name):
    conn = sqlite3.connect("Tracking.db")
    c = conn.cursor()
    today = date.today()


    if table == "history":
        c.execute(f"INSERT INTO {table} (name,date) VALUES (?,?)",(name,today))
    elif table == "routines":
        c.execute(f"INSERT INTO {table} (name) VALUES (?)",(name,))
        
    else: print("Table Does not exist")
    conn.commit()
    conn.close()


def display_options(title,options):
    print("\n")
    print("+-----------------------------------+")
    print(f"|          {title}")
    print("+-----------------------------------+")
    # For option in options do. The "i" is used because it counts up, enumerate enumerates the list starting from the number given (so it starts counting from 1 instead of 0).
    for i, option in enumerate(options, 1): 
        print(f"|  {i}. {option}") # if you ut the {} it will print a variable like text and again the f makes the string more fancy
    print("+-----------------------------------+")

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')


def update_menu():
    while True:
        Routines.print_table()

        opt = ["Delete Routine                |","Add Routine                   |","Go Back                       |"]
        display_options("    OPTIONS              |",opt)


        answer = input("---> ")

        if answer == "1":
            routine = input("Input the ID of the routine you want to delete --> ")
            delete_data(routine)
        elif answer == "2":
            clear_screen()
            Routines.print_table()

            new = input("Name of the New Routine?: ")
            insert("routines",new)
            clear_screen()

        elif answer == "3": 
            clear_screen()
            break
        else: 
            clear_screen() 
            print("Only Input Either 1 - 2 - 3")
        


