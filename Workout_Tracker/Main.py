import sqlite3
import DataBase 
import Routines
import History

def menu():

    # Are there better ways to do this maybe do i care not really meanwhile it works witouth trouble is fine
    menu_options = ["Show Available Routines       |", "Show Workout History          |", "Exit Program                  |"]
   
    while True:
        
        DataBase.make_table()
        DataBase.display_options("  Main Menu              |" , menu_options)
        
        answer = input("\n---> ")

        DataBase.clear_screen()
        if answer == "1": Routines.routines_table()
        elif answer == "2": History.history_table()
        elif answer == "3":
            print("")
            break
        else: print("Only Input Either 1 - 2 - 3")

        
if __name__ == "__main__": #uhm makes this module the main one
    menu()
