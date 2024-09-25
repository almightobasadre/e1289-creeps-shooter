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
    
    # Draw the Game
    display_surface.fill(color=(42, 62, 82)) # Charcoal: 43, 61, 79 / Night: All 10-22
    pygame.display.update()

pygame.quit()
