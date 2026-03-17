import pygame
import sys
from pygame.locals import * # Import useful constants like QUIT and KEYDOWN

# 1. Initialize Pygame
pygame.init()

# 2. Set up the display constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Basic Pygame Window")

# Define colors (RGB values)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up the clock to control frame rate
clock = pygame.time.Clock()
FPS = 60

# 3. Main game loop
running = True
while running:
    # A. Event handling
    for event in pygame.event.get():
        if event.type == QUIT: # If the user clicks the close button
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE: # If the user presses the Escape key
            running = False

    # B. Game logic (e.g., update object positions, check collisions)
    # This section is empty for a basic window

    # C. Drawing
    screen.fill(RED) # Fill the background with white
    # Draw other game elements here

    # D. Update the display
    pygame.display.flip() # Update the full display Surface to the screen

    # E. Cap the frame rate
    clock.tick(FPS)

# 4. Quit Pygame
pygame.quit()
sys.exit()
