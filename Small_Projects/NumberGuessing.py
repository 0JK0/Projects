import random

x = int(input("Enter a minimun number: "))
b = int(input("Enter a maximun number: "))

num = random.randrange(x,b)
amount = 0

running = True
while running:
    g = int(input("Your guess?: "))

    if g < num:
        print("Too small")
        amount =+ 1
    elif g > num:
        print("Too Big")
        amount =+ 1
    elif g == num:
        print("CORRECT!!! \nAmount of guesses: ",amount)
        running = False
