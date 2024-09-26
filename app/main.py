import pygame
# Only importing the function to use for performance
from os.path import join
from random import randint

# Initialize Pygame and set up the game window
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Creeps Shooter")
running = True

# # Plain Surface
# surf = pygame.Surface((50, 50))
# surf.fill('orange')
x = 100

# Import image using os.path.join() for cross-platform file path compatibility instead of hardcoding paths like "dir/dir/file"
# Use convert() for better performance, _alpha is added for images that have transparent pixels
player_surf = pygame.image.load(join('assets/art', 'player.png')).convert_alpha()
star_surf = pygame.image.load(join('assets/art', 'star.png')).convert_alpha()

# Generate random (x, y) positions for stars and store them in star_positions using List Comprehension
star_count = 22
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(star_count)] 

while running:
    # Event loop that keeps updating frames to display content until exiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the game components
    display_surface.fill(color=(43, 61, 79)) # Charcoal: 43, 61, 79 / Night: All 10-22
    x += 0.1
    display_surface.blit(player_surf, (x, 590))

    # Draw stars using their pre-generated list index
    for pos in star_positions:
        display_surface.blit(star_surf, (pos))

    pygame.display.update()

pygame.quit()
