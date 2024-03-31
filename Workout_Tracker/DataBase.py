import sqlite3
import os

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


def insert(table,name,date=None):
    conn = sqlite3.connect("Tracking.db")
    c = conn.cursor()

    if table == "history":
        c.execute(f"INSERT INTO {table} (name,date) VALUES (?,?)",(name, date))
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
    # For option in options do. The "i" is used because it counts up, enumerate enumerates the list starrting from the number given (so it starts counting from 1 instead of 0).
    for i, option in enumerate(options, 1): 
        print(f"|  {i}. {option}") # if you ut the {} it will print a variable like text and again the f makes the string more fancy
    print("+-----------------------------------+")

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
