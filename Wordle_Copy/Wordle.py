from random_word import Wordnik
import os
import random

class GameLogic:

    def __init__(self):
        self.split_word = []
        self.split_guess = []
        self.correct_letters = ["-","-","-","-","-"]
        self.misplaced = []
        self.past_guess = [[0] * 1 for i in range(4)]

    def clear_screen(self):
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_banner(self): # The ultimate epic GUI best gui desinger of 2024 here
        print("\n")
        print("+-----------------------------------+")
        print("|               Wordle              |")
        print("+-----------------------------------+")
        print("\n")

    def create_word(self): #gets the random word
        rw = Wordnik()
        word = rw.get_random_word(hasDictionaryDef = "true", minCorpusCount = 1000 ,minDictionaryCount =5  ,includePartOfSpeech = "verb", excludePartOfSpeech = "proper noun,name,acronym,noun", minLength = 5, maxLength = 5)
        #rw.word_of_the_day(date="2018-01-01")

        print(word)

        for letter in word:
            self.split_word.append(letter.lower()) #Splits the word by letter and put each letter as an item in a list

        return word


    def check(self): #Checks if the input is correct with the word by checking if the letter on the same index are the same
        for i in range(5):

            if self.split_guess[i] == self.split_word[i]:
                self.correct_letters[i] = self.split_guess[i] 

            if self.split_guess[i] != self.split_word[i]:
                self.correct_letters[i] = "-"

        for i in range(5):
            for element in self.split_guess:
                if element in self.split_word and element not in self.misplaced and element not in self.correct_letters :
                    self.misplaced.append(element)

        # print(" Split.Word: ",self.split_word, "\n Split.guess: ",self.split_guess, "\n Split.Correct_letters: ",self.correct_letters, "\n Split.misplaced: ",self.misplaced)


    def answer(self): #This just recives the input and divides it for the list
        guess = input("-->  ")

        for letter in guess:
            self.split_guess.append(letter.lower()) #Splits the word for the list
        
        #print("\n guess: ",guess)

    def keep(self):
        while True:

            self.clear_screen()
            self.display_banner()

            print("\n")
            for letter in self.correct_letters: #prints the divided guess but in a way it looks cool ig
                print(letter,end = " ")
            print("\n")
            

            random.shuffle(self.misplaced)
            print("Misplaced letters: ",self.misplaced)

            self.misplaced.clear()
            print("\n")

            break



    def play(self): #main game loop but inside a function for "goooood practice"
        while True:
            
            self.clear_screen()

            self.display_banner()

            word = self.create_word()
            print(word,"\n") #This should be taken out later tbh is just here for testing


            for row in self.past_guess:
                print(row)

           
            for i in range(4):

                self.answer()

                self.check()

                self.keep()

                attempts = 0
                self.past_guess[attempts][0] = self.correct_letters
                attempts += 1

                for row in self.past_guess:
                    print(row)

                self.split_guess.clear()
                
            break


if __name__ == "__main__":
    game = GameLogic()
    game.play()
