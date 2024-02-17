#Made by --> JK
#Could be better but ehh whatever


#Functions that do the math
def sum(a,b):
    return a + b
def res(a,b):
    return a - b
def multi(a,b):
 return a * b
def div(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cant Divide By Zero!!")

#Function that makes the programe run or re-run 
def next ():
    global x 
    
    Sigue = input("Do you want to continue runing the program? (Y / N): ").lower()
    if Sigue == "y" or Sigue == "yes":
        print (" \n You said Yes, The program continues: \n ")
        x = 1
        main()
    else:
        print (" \n Closing Program!!")
        x = 2
        
x = 1    

#Math options available in the program
options = ["1","addition","2","resta","3","multiplicacion","4","divicion"]

#Main loop where everythign is called and so
def main ():
    global x 
    while x == 1:
        selected = None
        #makes sure that the selected option is part of the options and do the needed math
        while selected not in options:
            selected = input(f"What do you want to do:\n" "1.Addition\n" "2.Resta\n" "3.Multiplicacion\n" "4.Divicion\n").lower()
            if selected not in options:
                print("\nPlease Choose An Available option")
            else:
                print(" ")
        
        numbers = input("Numbers: ") #Recives input as string
        operation= [] #Makes a list 
     
     #.extend: adds to the end of the list, Slipt: splits the string at the said
        try:
            operation.extend(numbers.split(" ")) 
            ope1 = operation[0]
            ope2 = operation[1]
        except IndexError:
            print("\n Use Two Numbers Separated By An Space!! \n")
            main()
    
 
      #does the correspoding operation
        if selected == "1" or  selected == "addition": 
         print ("Resultado Suma: ",sum (float(ope1),float(ope2)))
        elif selected == "2" or selected == "resta":
         print ("Resultado Resta: ",res (float(ope1),float(ope2))) 
        elif selected == "3" or selected == "multiplicacion":
         print ("Resultado Multiplicacion: ",multi (float(ope1),float(ope2)))
        elif selected == "4" or selected == "divicion":
         print ("Resultado Divicion: ",div (float(ope1),float(ope2)))
        else:
         print("This Is Not An Option!!")
     
        x = 2
        next()
             

main()    
     








