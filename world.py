
import settings
import pygame



def draw_map(lst_2D,color1,color2,surface):
    tile_rect=pygame.Rect(settings.POS_X,settings.POS_Y,settings.TILE_SIZE,settings.TILE_SIZE)
    for row in range(len(lst_2D)):
        for col in range(len(lst_2D[row])):
            tile_type=lst_2D[row][col]
            tile_rect.x,tile_rect.y=col*settings.TILE_SIZE ,row*settings.TILE_SIZE
            
            if tile_type==1:
                pygame.draw.rect(surface,color1,tile_rect)
            else:
                pygame.draw.rect(surface,color2,tile_rect)
    return
def get_tile_rects(lst_2D):
    tile_rect=[]
    for row in range(len(lst_2D)):
        for col in range(len(lst_2D[row])):
            if lst_2D[row][col] == 1:
                new_rect=col*settings.TILE_SIZE,row*settings.TILE_SIZE,settings.TILE_SIZE,settings.TILE_SIZE
                tile_rect.append(new_rect)
              #new_rect=pygame.Rect(col*settings.TILE_SIZE,row*settings.TILE_SIZE,
            #                      settings.TILE_SIZE,settings.TILE_SIZE)
                
    return(tile_rect)
    