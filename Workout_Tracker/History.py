import sqlite3
import DataBase 
import Routines


def print_table():
    routines = DataBase.show_table("history")

    print(" ")
    print("+------------------------------------+")
    print("|              HISTORY               |")
    print("+------------------------------------+")

    print("|\n|ID\tName\tDate") #\
    for row in routines:
        print(f"|{row[0]}\t{row[1]}\t{row[2]}")

def history_table():
    while True:

        print_table()

        opt = ["Update                        |","Delete                        |","Go Back                       |"]
        DataBase.display_options("    OPTIONS              |",opt)

        answer = input("---> ")

        if answer == "1":
            new = input("Routine? ---> ")

            DataBase.insert("history",new)
            DataBase.clear_screen()
        elif answer == "2":
            print("\n")
            DataBase.clear_screen()
            break
        else:
            print("Only Input Either 1 - 2")
            
            
            