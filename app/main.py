import pygame

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
Step 1: Initialize pygame.init() and screen properties, also always include pygame.quit()
Step 2: Setup the game event loop
Step 3: Draw the game objects using surface
"""