import DataBase
import sqlite3

def print_table():
    routines = DataBase.show_table("routines")

    print("")
    print("+------------------------------------+")
    print("|              ROUTINES              |")
    print("+------------------------------------+")

    print("|\n|ID\tName") #\
    for row in routines:
        print(f"|{row[0]}\t{row[1]}")
    print("+------------------------------------+")
    

def routines_table():
    while True:

        print_table()

        opt = ["Use Routine                   |","Update                        |","Go Back                       |"]
        DataBase.display_options("    OPTIONS              |",opt)

        answer = input("---> ")

        if answer == "1":
            DataBase.clear_screen()
            print_table()

            id = input("Input the ID of the routine you want to use --> ")

            routine_name = DataBase.get_routine_name(id)
            
            DataBase.insert("history",routine_name)

            DataBase.clear_screen()
            print("\n Everything Was Successful!!")


        elif answer == "2":
            DataBase.clear_screen()
            DataBase.update_menu()
        elif answer == "3":
            print("\n")
            DataBase.clear_screen()
            break
        else:
            print("Only Input Either 1 - 2 - 3")
            
            
