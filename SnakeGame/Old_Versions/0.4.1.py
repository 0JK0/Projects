import pygame  
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
width, height =  1280,  720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GSnake Game  0.2") #Name of the window

running = True

# Player position
player_pos = pygame.Vector2(screen.get_width() /  2, screen.get_height() /  2)
player_direction = pygame.Vector2(0,0)

# Initial apple position
apple_pos = pygame.Vector2(random.randrange(0,1280), random.randrange(0,720))

# Define colors
green = (0,255,  0)
red = (255,0,0)
white = (255,255,255)

# Define the close distance threshold
close_distance_threshold =  50  # Change this value as needed

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calculate the distance between the player and the apple
    distance_x = abs(player_pos.x - apple_pos.x)
    distance_y = abs(player_pos.y - apple_pos.y)
    distance = (distance_x**2 + distance_y**2)**0.5

    if distance <= close_distance_threshold:
        # Move the apple to a new random position
        apple_pos.x = random.randrange(0,  1280)
        apple_pos.y = random.randrange(0,  720)

    # Fill the window with green
    screen.fill(green)

    # Draw the player
    player_rect = pygame.Rect(player_pos.x, player_pos.y,  20,  20)
    pygame.draw.rect(screen, red, player_rect)

    # Draw the apple
    apple = pygame.Rect(apple_pos.x, apple_pos.y,  20,  20)
    pygame.draw.rect(screen, white, apple)

    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_direction.y = -0.5
        player_direction.x =  0
    elif keys[pygame.K_s]:
        player_direction.y =  0.5
        player_direction.x =  0
    elif keys[pygame.K_a]:
        player_direction.x = -0.5
        player_direction.y =  0
    elif keys[pygame.K_d]:
        player_direction.x =  0.5
        player_direction.y =  0

    player_pos += player_direction

    # Update the display
    pygame.display.flip()
