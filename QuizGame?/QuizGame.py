#The answers to the questions
answer = ["A","B","C"]

#The Questions past mentiones
questions = ["Are you gay? \n A.Yes \n B.No \n C.Maybe \n",  "Did you lie? \n A.Perhaps \n B.Nein \n C.Indeed \n",  "Do you promise? \n A.I Promise \n B.No Please peg me \n C.UwU \n"]

#Here are saved the user answers to later be comapared
guesses = []
correct = 0

#Function that prints a list from a start to a stop
def PrintList(List,start,stop):
    for x in range(start,stop):
        print (List[x])
        #x stores the range (0 , 3) and then gives that range to the list
        
        
#A fuction that compares a string input(variable) to a dictionary(dictionary) and a specific key on this(key)
def check(variable,dictionary,key):
    global correct
    guesses.append(variable)
    if variable == dictionary[key]:
        correct += 1
        return 1 
    else:
        return 0


# The while loop will finish if the function return(finish) something, so if it goes to "else:" the function returs nothing wich means  it will repeat again
def ask(QN):
    while True:
        n = input(QN).upper()
        if n in answer:
            return n
        else:
            print("Please Choose An Available Option, Remeber Only Input The Letter \n -------------------------------------------Same Question-------------------------------------------")

#its just the loop not much to say
def loop():
    for i in range(len(questions)): 
        result = check(ask(questions[i]),answer,i)
        print("-------------------------------------------Next Question-------------------------------------------")
    
        
        
#well the main fuction
def main():
    again = "Y"
    
    while again == "Y":
        loop()

        print("\n You Got ",correct," Answers Right")
        print("\n Correct Answers:", end=" ")
        for i in answer: print (i , end=" ")

        print("\n Your Answers:", end=" ")
        for i in guesses: print (i , end=" ")

        print("\n \n Your Note  Is:", str(correct*100 / len(answer))+"%") #calculates your porcentage

        again = input("Do you want to repeat again? (Y/N): ").upper()
    
    
        if again == "Y":
            print("\n -------------------------------------------RE-DO-------------------------------------------")
            main()
        else:
            print("Byeeeeee <3")
        
        
        
main()
