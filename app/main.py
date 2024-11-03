import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # only display once

running = True

while running:
    for event in pygame.event.get(): # game loop
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

"""
Step 1: Initialize pygame.init() and screen properties, also always include pygame.quit()
Step 2: Setup the game event loop and draw the game objects
"""