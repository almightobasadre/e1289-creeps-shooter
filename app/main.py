import pygame

# General Setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True

while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type ==    pygame.QUIT:
            running = False

pygame.quit()
