import pygame 
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GSnake Game 1") #Name of the window

running = True

# Basically just calculates the position of the player according to the 
#divides the width of the screen by 2 and the height of the screen by 2 so for example -> 1280 / 2 = 640, 720 / 2 = 360
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) #oh no math
#print (player_pos), result [640, 360]

player_direction = pygame.Vector2(0,0)

#set the position of the apple (random)
apple_pos = pygame.Vector2(random.randrange(0,1280),random.randrange(0,720))

# Define colors
green = (0,255, 0)
red = (255,0,0)
white = (255,255,255)


# Main game loop
while running:
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    if player_pos.x == apple_pos.x and player_pos.y == apple_pos.y:
        # Move the apple to a new random position
        apple_pos.x = random.randrange(0,  1280)
        apple_pos.y = random.randrange(0,  720)


    # Fill the window with green
    screen.fill(green)

    #Makes the dammed rectangle
    player_rect = pygame.Rect(player_pos.x, player_pos.y,20,20)
    pygame.draw.rect(screen, red, player_rect)
    
 
 
    #Makes the future to be apple
    apple = pygame.Rect(apple_pos.x,apple_pos.y,20,20)
    pygame.draw.rect(screen,white,apple)
      
   
    # Player Movement -- Using "Elif" contrary to several "If" makes it so only one can happen at the same time
    # Using "= -1" and not "-= 1" makes it so the movement is instant and it doesnt build up speed
    # resets the contrary speed to 0 so no diagonal or build up movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_direction.y = -0.5
        player_direction.x = 0
    elif keys[pygame.K_s]:
        player_direction.y = 0.5
        player_direction.x = 0
    elif keys[pygame.K_a]:
        player_direction.x = -0.5
        player_direction.y = 0
    elif keys[pygame.K_d]:
        player_direction.x = 0.5
        player_direction.y = 0
  
    player_pos += player_direction  

    # Check if the player has eaten the apple
  


    # Updates the display if taken out everything goes black
    pygame.display.flip()
    

