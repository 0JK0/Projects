import pygame 
import sys
import random
import time


#-------------
# Initialize Pygame 
pygame.init()


#-------------
#Grids?
COLUMNS, ROWS, SIZE = 35,30,20
dire = [100,100] #initial point
snake_body = [dire[:]] #defines the snakes body

#-------------
#Sets up the window
screen = pygame.display.set_mode((COLUMNS*SIZE, ROWS*SIZE))#(700 , 600)
pygame.display.set_caption("Snake Game v1.2")# not alot of differences between versions,altough im a workaholic but since im just learning everything takes a looong while

#-------------
# Define colors
green = (0,255, 0)
red = (255,0,0)
white = (255,255,255)
blue = (0,0,255)

#-------------
#Random stuff that need to be here
last_key = pygame.K_k
doOnce = True

#-------------
eaten_apple = True
# Main game loop
running = True
while running:

    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #If something happens and that something is a key being pressed do:    
    if event.type == pygame.KEYDOWN:
        last_key = event.key # event.key is the storage for the ID of the pressed key

    #sets the speed
    clock = pygame.time.Clock()
    clock.tick(100)
    


    #-------------
    ##MOVEMENT
   
    #Continues Movement (simplified)
    if last_key == pygame.K_RIGHT: dire [0] += 1
    elif last_key == pygame.K_LEFT:  dire [0] -= 1 
    elif last_key == pygame.K_UP:  dire [1] -= 1   
    elif last_key == pygame.K_DOWN:  dire [1] += 1
    if last_key == pygame.K_BACKSPACE: snake_body.append(snake_body[-1])


    snake_x = dire[0]
    snake_y = dire [1]


        
    #-------------
    ##DRAW STUFF
            



    #Draws the walls (could be done better)
    def walls(x,y,size1,size):
        walls = pygame.Rect(x,y,size1,size)
        w = pygame.draw.rect (screen,white,walls)
        return w

    right = walls (692,1,10,700) 
    left = walls (1,1,10,700) 
    top = walls (1,1,700,10) 
    bottom = walls (1,592,700,10) 
    


    #Draws the head of the snake
    snake = pygame.Rect(snake_x,snake_y,20,20)
    pygame.draw.rect(screen,green,snake)

    
    #-------------
    #COLLISIONS

    if doOnce == True:
        apple_y = random.randrange(1,(COLUMNS * SIZE)) # keeps in the grid
        apple_x = random.randrange (1,(ROWS * SIZE))
        doOnce = False


    fake_keypress_event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_BACKSPACE})
    
    if (
        snake_x < apple_x + 10 
        and snake_x + 20 > apple_x 
        and snake_y < apple_y + 10 
        and snake_y + 20 > apple_y 
    ):
        snake_body = [dire[:]] + snake_body[:-1]
        apple_x = random.randrange(1, (ROWS * SIZE)) # Randomizes the position of the apple, i know how this one works i did this myself
        apple_y = random.randrange(1, (COLUMNS * SIZE))
        pygame.event.post(fake_keypress_event)
    

    if eaten_apple:
        snake_body.append(snake_body[-1])
        eaten_apple = False

    snake_body.insert(0, dire[:])  # Insert the current position to the beginning of the list
    if len(snake_body) > 1: #if the list is bigger than 1
        del snake_body[-1] # deletes the beggining part of a list

    
    # Copy the current direction (head) and create a new list
    snake_body = [dire[:]] + snake_body[:-1]  # Update the snake's body by appending the new head and excluding the last part
   

    #Stop the game when                       
    def stop():
        global running
        running = False

    def colission(moves,stays):
        if pygame.Rect.colliderect(moves,stays):
            stop()

    colission(snake,right)
    colission(snake,left)
    colission(snake,top)
    colission(snake,bottom)


    #-------------
    ##BODY GROWTH

    #sets up a loop to go through each part of the snake's body.
    for part in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(part[0], part[1], 20, 20))
    

    #-------------
    #Draws The apple  
    apple = pygame.Rect(apple_x,apple_y,10,10)
    pygame.draw.rect(screen,red,apple)

    pygame.display.flip()


