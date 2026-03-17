import pygame
import sys

# 1. Setup
pygame.init()
tile_size = 16
scale = 2  # Making it big so you can see the pixels clearly
width, height = 20 * tile_size, 15 * tile_size
screen = pygame.display.set_mode((width * scale, height * scale))
pygame.display.set_caption("Tile Render Test")

# 2. Load the image (Ensure the filename is exactly correct)
try:
    tileset_img = pygame.image.load("assets/images/Terrain/Terrain.png").convert_alpha()
except:
    print("Error: Could not find 'Terrain (16x16).png' in this folder!")
    sys.exit()

# 3. Function to cut a specific tile
def get_tile(col, row):
    # Create a transparent 16x16 surface
    #surface = pygame.Surface((16, 16), pygame.SRCALPHA)
    surface = pygame.Surface((16, 16)).convert()
    surface.set_colorkey((0, 0, 0))
    # Area = (x_start, y_start, width, height)
    surface.blit(tileset_img, (0, 0), (col * 16, row * 16, 16, 16))
    return surface

# Define some tiles from your image
grass_top = get_tile(6, 0)   # Green Grass
dirt_block = get_tile(6, 1)  # Brown Dirt
brick_red = get_tile(18, 5)  # Red Bricks
# Updated coordinates for a smoother look
# These match the grass section in your image (Columns 6, 7, 8)
grass_left   = get_tile(6, 0)
grass_mid    = get_tile(7, 0)
grass_right  = get_tile(8, 0)
dirt_mid     = get_tile(7, 1) # Solid dirt for underneath

# Extracting Stone
stone_block = get_tile(0, 0)
stone_wall  = get_tile(1, 1)

# Extracting Steel (Yellow Metal)
steel_block = get_tile(18, 8)
steel_bolt  = get_tile(18, 9)

# If you want the grey/blue metal plates:
metal_grey  = get_tile(12, 4)

stone_block = get_tile(0, 0)
steel_top = get_tile(19, 8)
steel_bot = get_tile(19, 9)
metal_plat = get_tile(13, 4)

# 4. Small Map (0 = Sky, 1 = Grass, 2 = Dirt, 3 = Brick)
'''small_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 3, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 2, 2, 2, 0, 0, 2, 2, 2, 0],
]'''	
# 1=Left, 2=Middle, 3=Right, 4=Solid Dirt
'''big_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 0],
    [0, 0, 0, 0, 0, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 2, 3, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 0, 0, 0],
    [0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 6, 6, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 6, 6, 0],
    [0, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7],
    [8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8],
    [0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 3],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
]'''

big_map = [
    [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], # Stone Ceiling
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 5, 5, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 5, 5, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 7, 7, 7, 7, 0, 0, 1, 2, 2, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 8, 8, 8, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 1, 2, 3],
    [4, 4, 4, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, 0, 0],
    [0, 0, 1, 2, 2, 2, 3, 0, 0, 6, 6, 0, 0, 4, 4, 4, 4, 4, 0, 0],
    [1, 2, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3], # Floor
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    ]

# Create a small canvas to draw on first
canvas = pygame.Surface((width, height))

# 5. Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    canvas.fill((135, 206, 235)) # Sky Blue

    # Rendering the map using range loops
    for r in range(len(big_map)):
        for c in range(len(big_map[r])):
            tile_type = big_map[r][c]
            
            x_pos = c * tile_size
            y_pos = r * tile_size

            if tile_type == 1: canvas.blit(grass_left, (x_pos, y_pos))
            elif tile_type == 2: canvas.blit(grass_mid, (x_pos, y_pos))
            elif tile_type == 3: canvas.blit(grass_right, (x_pos, y_pos))
            elif tile_type == 4: canvas.blit(dirt_mid, (x_pos, y_pos))
            elif tile_type == 5: canvas.blit(brick_red, (x_pos, y_pos))
            elif tile_type == 6: canvas.blit(stone_block, (x_pos, y_pos))
            elif tile_type  == 7: canvas.blit(steel_top, (x_pos, y_pos))
            elif tile_type  == 8: canvas.blit(steel_bot, (x_pos, y_pos))
            elif tile_type  == 9: canvas.blit(metal_plat, (x_pos, y_pos))

    # Scale the canvas up to the screen size
    scaled_surf = pygame.transform.scale(canvas, (width * scale, height * scale))
    screen.blit(scaled_surf, (0, 0))
    
    pygame.display.flip()