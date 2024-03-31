import DataBase

def show_table():
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

        show_table()

        opt = ["Update                        |","Delete                        |","Go Back                       |"]
        DataBase.display_options("    OPTIONS              |",opt)

        answer = input("---> ")

        if answer == "1":
            new = input("---> ")
            DataBase.insert("routines",new)
            DataBase.clear_screen()
        elif answer == "2":
            DataBase.clear_screen()
        elif answer == "3":
            print("\n")
            DataBase.clear_screen()
            break
        else:
            print("Only Input Either 1 - 2 - 3")
            
            