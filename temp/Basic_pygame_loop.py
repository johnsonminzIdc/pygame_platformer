#import library
import pygame
import sys
from asset_loader import Asset_loader
#initailised pygame library
pygame.init()
Scale=3
width , height=320,256
#create game window
screen=pygame.display.set_mode((Scale*width,Scale*height))
canvas=pygame.Surface((width,height)).convert()
pygame.display.set_caption("johnson game")
#RED=(255,0,0)
x=10
tile_size=16
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
level_map=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,0,1,1],
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
    
   #create map
    for x in range(len(level_map)):
        for y in range(len(level_map[x])):
            tile_type=level_map[x][y] #remember this is how we can use 2D array
            if tile_type==1:
                gnd_rect=pygame.Rect(y*tile_size,x*tile_size,tile_size,tile_size)
    
                #pygame.draw.rect(canvas,BROWN,ground_rect)
                if player_rect.colliderect(gnd_rect):
                    if current_velocity_y>0:
                        player_rect.bottom=gnd_rect.top
                        current_velocity_y=0
                        is_jumping=0
                        #Player_current_state="Idle"

    canvas.fill(BLUE)
    for row in range(len(level_map)):
        for col in range(len(level_map[row])):
            if level_map[row][col] == 1:
                pygame.draw.rect(canvas,BROWN,(col*tile_size,row*tile_size,tile_size,tile_size))
    
    

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