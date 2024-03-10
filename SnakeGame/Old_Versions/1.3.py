import pygame 
import sys
import random

# Initialize Pygame and Sets up the window
pygame.init()

#Grids?
COLUMNS, ROWS, SIZE = 35,30,20
body = [(COLUMNS//2 , ROWS//2)]
dire = [10,20]
   

screen = pygame.display.set_mode((COLUMNS*SIZE, ROWS*SIZE))#(700 , 600)
pygame.display.set_caption("Snake Game v1.3")# not alot of differences between versions,altough im a workaholic but since im just learning everything takes a looong while

last_key = pygame.K_k


doOnce = True

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


    ##MOVEMENT
   
    #Continues Movement (simplified)
    if last_key == pygame.K_RIGHT: dire [0] += 1
    elif last_key == pygame.K_LEFT:  dire [0] -= 1 
    elif last_key == pygame.K_UP:  dire [1] -= 1   
    elif last_key == pygame.K_DOWN:  dire [1] += 1

    snake_x = dire[0]
    snake_y = dire [1]

    #Stop the movement when x happens
    def stop(): 
        dire [0] + 0
        dire [1] + 0

   

    #DRAW STUFF
            
    # Define colors
    green = (0,255, 0)
    red = (255,0,0)
    white = (255,255,255)

    screen.fill((0,0,0))


    #Draws the walls (could be done better)
    def walls(x,y,size1,size):
        walls = pygame.Rect(x,y,size1,size)
        pygame.draw.rect (screen,white,walls)

    walls (692,1,10,700) #Right
    walls (1,1,10,700) #left
    walls (1,592,700,10) #Top
    walls (1,1,700,10) #Bottom

    #Draws the head of the snake
    snake = pygame.Rect(snake_x,snake_y,20,20)
    pygame.draw.rect(screen,green,snake)

    #Draws The apple    

    
    if doOnce == True:
        apple_y = random.randrange(1,(COLUMNS * SIZE)) # keeps in the grid
        apple_x = random.randrange (1,(ROWS * SIZE))
        doOnce = False



    if (
        snake_x < apple_x + 10 
        and snake_x + 20 > apple_x 
        and snake_y < apple_y + 10 
        and snake_y + 20 > apple_y 
    ):
        apple_x = random.randrange(1, (ROWS * SIZE)) # Randomizes the position of the apple, i know how this one works i did this myself
        apple_y = random.randrange(1, (COLUMNS * SIZE))
        # Digamos que "S" esta en la posicion x5
        # Si le sumamos a si mismo su size (20)
        # este lanza un "rayo" hasta x25
        # Y si este rayo va mas alla que "A"(x10)
        # Enonces es correcto
        #Graphic and translated explanaition in the Documentation File


        
    apple = pygame.Rect(apple_x,apple_y,10,10)
    pygame.draw.rect(screen,red,apple)
    
    pygame.display.flip()

    #sets the speed
    clock = pygame.time.Clock()
    clock.tick(100)
