
import settings
import pygame


def tile_type(sheet,tile_x,tile_y):
    # Creates a small 16x16 surface
    surface = pygame.Surface((16, 16)).convert()
    surface.set_colorkey((0,0,0))
    #blit small surface out of the loaded texture
    surface.blit(sheet,(0,0),(tile_x*settings.TILE_SIZE,tile_y*settings.TILE_SIZE,settings.TILE_SIZE,settings.TILE_SIZE))
    return surface
    
    
    


def draw_map(lst_2D,tile_sheet,color2,surface):
        ##items
    grass_top = tile_type(tile_sheet,6, 0)   # Green Grass
    dirt_block = tile_type(tile_sheet,6, 1)  # Brown Dirt
    brick_red = tile_type(tile_sheet,18, 5)  # Red Bricks
    # Updated coordinates for a smoother look
    # These match the grass section in your image (Columns 6, 7, 8)
    grass_left   = tile_type(tile_sheet,6, 0)
    grass_mid    = tile_type(tile_sheet,7, 0)
    grass_right  = tile_type(tile_sheet,8, 0)
    dirt_mid     = tile_type(tile_sheet,7, 1) # Solid dirt for underneath

    # Extracting Stone
    stone_block = tile_type(tile_sheet,0, 0)
    stone_wall  = tile_type(tile_sheet,1, 1)

    # Extracting Steel (Yellow Metal)
    steel_block = tile_type(tile_sheet,18, 8)
    steel_bolt  = tile_type(tile_sheet,18, 9)

    # If you want the grey/blue metal plates:
    metal_grey  = tile_type(tile_sheet,12, 4)

    stone_block = tile_type(tile_sheet,0, 0)
    steel_top = tile_type(tile_sheet,19, 8)
    steel_bot = tile_type(tile_sheet,19, 9)
    metal_plat = tile_type(tile_sheet,13, 4)

    tile_rect=pygame.Rect(settings.POS_X,settings.POS_Y,settings.TILE_SIZE,settings.TILE_SIZE)
    for row in range(len(lst_2D)):
        for col in range(len(lst_2D[row])):
            tile_id=lst_2D[row][col]
            #tile_rect.x,tile_rect.y=col*settings.TILE_SIZE ,row*settings.TILE_SIZE
            x_pos=col*settings.TILE_SIZE
            y_pos=row*settings.TILE_SIZE
            if tile_type!=0:
                if tile_id == 1: surface.blit(grass_left, (x_pos, y_pos))
                elif tile_id == 2: surface.blit(grass_mid, (x_pos, y_pos))
                elif tile_id == 3: surface.blit(grass_right, (x_pos, y_pos))
                elif tile_id == 4: surface.blit(dirt_mid, (x_pos, y_pos))
                elif tile_id == 5: surface.blit(brick_red, (x_pos, y_pos))
                elif tile_id == 6: surface.blit(stone_block, (x_pos, y_pos))
                elif tile_id  == 7: surface.blit(steel_top, (x_pos, y_pos))
                elif tile_id  == 8: surface.blit(steel_bot, (x_pos, y_pos))
                elif tile_id  == 9: surface.blit(metal_plat, (x_pos, y_pos))
    

            else:
                pygame.draw.rect(surface,color2,tile_rect)
    return
def get_tile_rects(lst_2D):
    tile_rect=[]
    for row in range(len(lst_2D)):
        for col in range(len(lst_2D[row])):
            if lst_2D[row][col] != 0:
                new_rect=col*settings.TILE_SIZE,row*settings.TILE_SIZE,settings.TILE_SIZE,settings.TILE_SIZE
                tile_rect.append(new_rect)
              #new_rect=pygame.Rect(col*settings.TILE_SIZE,row*settings.TILE_SIZE,
            #                      settings.TILE_SIZE,settings.TILE_SIZE)
                
    return(tile_rect)
    