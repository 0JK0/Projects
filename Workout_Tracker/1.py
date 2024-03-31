import sqlite3

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


def insert(table,name):
    conn = sqlite3.connect("Tracking.db")
    c = conn.cursor()
    c.execute(f"INSERT INTO {table} (name) VALUES (?)",(name,))
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

    

def menu():
    # Are there better ways to do this maybe do i care not really meanwhile it works witouth trouble is fine
    menu_options = ["Show Available Routines       |", "Show Workout History          |", "Exit Program                  |"]
   
    while True:
        make_table()

        display_options("  Main Menu              |" , menu_options)

        answer = input("\n---> ")

        if answer == "1":

            routines = show_table("routines")

            print("")
            print("+------------------------------------+")
            print("|              ROUTINES              |")
            print("+------------------------------------+")


            print("|\n|ID\tName") #\
            for row in routines:
                print(f"|{row[0]}\t{row[1]}")

        elif answer == "2":
            
            routines = show_table("history")

            print(" ")
            print("+------------------------------------+")
            print("|              HISTORY               |")
            print("+------------------------------------+")

            print("|\n|ID\tName\tDate") #\
            for row in routines:
                print(f"|{row[0]}\t{row[1]}\t{row[2]}")

        elif answer == "3":

            print("")
            break

        else:

            print("Only Input Either 1 - 2 - 3")
        


if __name__ == "__main__": #uhm makes this module the main one
    menu()
