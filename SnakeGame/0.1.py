import pygame 
import sys

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GSnake Game 0.1") #Name of the window

running = True

# Basically just calculates the position of the player according to the 
#divides the width of the screen by 2 and the height of the screen by 2 so for example -> 1280 / 2 = 640, 720 / 2 = 360
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) #oh no math
#print (player_pos), result [640, 360]

# Define colors
green = (0, 255, 0)
red = (255,0 , 0)

# Main game loop
while running:
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the window with green
    screen.fill(green)

    #Makes the dammed rectangle
    player_rect = pygame.Rect(player_pos.x, player_pos.y,60,40)
    pygame.draw.rect(screen, red, player_rect)
    
    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 1
    if keys[pygame.K_s]:
        player_pos.y += 1
    if keys[pygame.K_a]:
        player_pos.x -= 1 
    if keys[pygame.K_d]:
        player_pos.x += 1 


    # Updates the display if taken out everything goes black
    pygame.display.flip()
    

