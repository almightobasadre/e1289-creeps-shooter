import pygame
# Only importing the function to use for performance
from os.path import join

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # only display once
pygame.display.set_caption("Creeps Shooter")

running = True

# Plain Surface
surf = pygame.Surface((50, 50))
surf.fill('blue')
x = 100

# Use convert() for better performance, _alpha is added for images that have transparent pixels
player_sprite = pygame.image.load(join('assets/art', 'b2_godot.png'))

while running:
    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT:
            running = False
        
    # draw the game
    screen.fill(color = (43, 61, 79))
    x += 0.1
    screen.blit(surf, (x, 150))

    pygame.display.flip()

pygame.quit()

"""
Step 1: Initialize pygame and setup the game window, also always include pygame.quit()
Step 2: Setup the game event loop
Step 3: Import image using os.path.join() for cross-platform file path compatibility instead of hardcoding paths like "dir/dir/file"
Step 4: Draw the game objects using surface
"""