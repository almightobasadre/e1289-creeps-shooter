import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # only display once
pygame.display.set_caption("Creeps Shooter")

running = True

while running:
    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT:
            running = False
        
    # draw the game
    screen.fill(color = (43, 61, 79))
    pygame.display.flip()

pygame.quit()

"""
Step 1: Initialize pygame.init() and screen properties, also always include pygame.quit()
Step 2: Setup the game event loop and draw the game objects
"""