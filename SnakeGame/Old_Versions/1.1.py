import pygame 
import sys
import random

# Initialize Pygame and Sets up the window
pygame.init()

#Grids?
COLUMNS, ROWS, SIZE = 35,30,20

# Define colors
green = (0,255, 0)
red = (255,0,0)
white = (255,255,255)

screen = pygame.display.set_mode((COLUMNS*SIZE, ROWS*SIZE)) #(700 , 600)
pygame.display.set_caption("Snake Game v1.1")

length = 1

body = [(COLUMNS//2 , ROWS//2)]

#divides the width(COLUMNS) of the screen by 2 and the height(ROWS) of the screen by 2 so for example
#print (body), result [17, 15]
#Direction , starting direction "Right"
# dir = (A , B) A is the x(COLUMNS) axis and B is the y(ROWS) axis

dire = [10 , 20]

last_key = pygame.K_k

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
    
    def stop():
        if last_key == pygame.K_BACKSPACE: 
            dire [0] = dire [0]
            dire [1] = dire [1]


    #Continues Movement (simplified)
    if last_key == pygame.K_RIGHT: dire [0] += 1
    elif last_key == pygame.K_LEFT:  dire [0] -= 1 
    elif last_key == pygame.K_UP:  dire [1] -= 1   
    elif last_key == pygame.K_DOWN:  dire [1] += 1
    
    stop()

    snake_x = dire [0]
    snake_y = dire [1]

    
    
        
    screen.fill((0,0,0))

    #Draws stuff

    def walls(x,y,size1,size):
        walls = pygame.Rect(x,y,size1,size)
        pygame.draw.rect (screen,white,walls)

    walls (692,1,10,700) #Right
    walls (1,1,10,700) #left
    walls (1,592,700,10) #Top
    walls (1,1,700,10) #Bottom
    
    snake = pygame.Rect(snake_x,snake_y,20,20)
    pygame.draw.rect(screen,green,snake)
    
    pygame.display.flip()
        
    



        

