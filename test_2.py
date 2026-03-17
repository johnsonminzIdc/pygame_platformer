#import library
import pygame
import sys
from asset_loader import Asset_loader
#initailised pygame library
pygame.init()
Scale=1
row,col=16,20
tile_size=16
width , height=tile_size*col,tile_size*row
#create game window
screen=pygame.display.set_mode((Scale*width,Scale*height))
canvas=pygame.Surface((width,height)).convert()
pygame.display.set_caption("johnson game")
#RED=(255,0,0)
x=10
#test funtion
# Load the tileset once at the top of your script
tileset_img = pygame.image.load("assets/images/Terrain/Terrain.png").convert_alpha()

bg_tile_img = pygame.image.load("assets/images/Terrain/Terrain.png").convert_alpha()

def get_tile(x_tile, y_tile):
    # Creates a small 16x16 surface
    surface = pygame.Surface((16, 16)).convert()
    #surface = pygame.Surface((16, 16)).convert()

    # Blits the portion of the tileset onto the small surface
    # Grass top-left is roughly at x=6, y=0 in your image
    surface.set_colorkey((0,0,0))
    surface.blit(tileset_img, (0, 0), (x_tile * 16, y_tile * 16, 16, 16))
    return surface

# Define the tile you want to use
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
#player is recangle 50 x 50
player_position_x,player_position_y=x,50
player_height,player_width=27,22
#player_rect = pygame.Rect(x, y, width, height)
player_rect=pygame.Rect(player_position_x,player_position_y,player_width,player_height)
player_anm={"Run":Asset_loader("assets/images/Entity/Player/Run.png",32,32).load(),"Jump":Asset_loader("assets/images/Entity/Player/Jump.png",32,32).load(),
            "Hit":Asset_loader("assets/images/Entity/Player/Hit.png",32,32).load(),"Idle":Asset_loader("assets/images/Entity/Player/Idle.png",32,32).load()}
is_jumping=0
gravity=0.8
velocity_x=1.5
velocity_y=8
current_velocity_y=0
floor_position_x,floor_position_y=0,100
BLUE= (135,206,235)
BROWN= (150 ,75,0)
#print(dir(a),type(a),type(b),type(f),a[1],f["key1"])
pos_x,pos_y=0,0
#sky_rect=pygame.Rect(pos_x,pos_y,tile_size,tile_size)
#ground_rect=pygame.Rect(pos_x,pos_y,tile_size,tile_size)
#ground_rect=pygame.Rect(pos_x,pos_y,tile_size,tile_size)
#sky_rect=pygame.Rect(pos_x,pox_y,tile_size,tile_size)
big_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Stone Ceiling
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 1, 2, 3],
    [4, 4, 4, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3, 0, 0],
    [0, 0, 1, 2, 2, 2, 3, 0, 0, 0, 0, 0, 6, 4, 4, 4, 4, 4, 6, 0],
    [1, 2, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 2, 3], # Floor
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    ]

#player_height,player_width
#pygame.draw.rect(surface, color, rect)
#create a while true loop
clock=pygame.time.Clock()
Player_current_state="Idle"
frame_index=0.0
offset_x,offset_y=5,5
Player_direction=1 #1 stand for facing right
ann_speed = 0.35
while True:
    if is_jumping==0:
        Player_current_state="Idle"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and is_jumping==0:
                #print("Jump",is_jumping)
                is_jumping=1
                #print("Jump",is_jumping)
                current_velocity_y= -velocity_y
                Player_current_state="Jump"
            
    
    keys=pygame.key.get_pressed()
    move_x=0
    
    if keys[pygame.K_LEFT]:
        move_x=-velocity_x
        Player_current_state="Run"
        Player_direction = -1
    if keys[pygame.K_RIGHT]:
        move_x=+velocity_x
        Player_current_state="Run"
        Player_direction =1
    player_rect.x += move_x
    if player_rect.right>=width:
        player_rect.right=width
    if player_rect.left <=0:
        player_rect.left=0
    #vertical movement
    current_velocity_y+=gravity
    player_rect.y +=  current_velocity_y    
    canvas.fill(BLUE)
   #create map
    for x in range(len(big_map)):
        for y in range(len(big_map[x])):
            tile_type=big_map[x][y] #remember this is how we can use 2D array
            x_pos,y_pos= y*tile_size,x*tile_size
            if tile_type !=0:
                gnd_rect=pygame.Rect(x_pos,y_pos,tile_size,tile_size)
                if tile_type == 1: canvas.blit(grass_left, (x_pos, y_pos))
                elif tile_type == 2: canvas.blit(grass_mid, (x_pos, y_pos))
                elif tile_type == 3: canvas.blit(grass_right, (x_pos, y_pos))
                elif tile_type == 4: canvas.blit(dirt_mid, (x_pos, y_pos))
                elif tile_type == 5: canvas.blit(brick_red, (x_pos, y_pos))
                elif tile_type == 6: canvas.blit(stone_block, (x_pos, y_pos))
                elif tile_type  == 7: canvas.blit(steel_top, (x_pos, y_pos))
                elif tile_type  == 8: canvas.blit(steel_bot, (x_pos, y_pos))
                elif tile_type  == 9: canvas.blit(metal_plat, (x_pos, y_pos))
    
                #pygame.draw.rect(canvas,BROWN,ground_rect)
                if player_rect.colliderect(gnd_rect):
                    if current_velocity_y>0:
                        player_rect.bottom=gnd_rect.top
                        current_velocity_y=0
                        is_jumping=0
                        #Player_current_state="Idle"
            #else:
                

    
    '''for row in range(len(big_map)):
        for col in range(len(big_map[row])):
            if big_map[row][col] == 1:
                #pygame.draw.rect(canvas,BROWN,(col*tile_size,row*tile_size,tile_size,tile_size))
                canvas.blit(grass_top, (x * tile_size, y * tile_size))'''
    

    #if player_rect.top <=0:
    #   player_rect.top=0
    #player animation 
    frames=player_anm[Player_current_state]
    current_ann=player_anm[Player_current_state]
    image_draw =current_ann[int(frame_index)%len(current_ann)]
    image_draw=pygame.transform.scale_by(image_draw,Scale)
    #animation oof player inverion
    if Player_direction ==-1:
        image_draw=pygame.transform.flip(image_draw,True,False)
    #draw world  
    scaled_canvas=pygame.transform.scale(canvas,(Scale*width,Scale*height))
    screen.blit(scaled_canvas,(0,0))
    #draw player
    screen.blit(image_draw,(Scale*(player_rect.x -offset_x),Scale*(player_rect.y-offset_y)))
    frame_index += ann_speed 
    pygame.display.flip()
    
    clock.tick(60)

pygame.display.update()

