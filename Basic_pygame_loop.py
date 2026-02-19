#import library
import pygame
import sys
from asset_loader import Asset_loader
#initailised pygame library
pygame.init()
#create game window
screen=pygame.display.set_mode((2*160,2*128))
pygame.display.set_caption("johnson game")
#RED=(255,0,0)
x=10
tile_size=2*16
#player is recangle 50 x 50
player_position_x,player_position_y=x,50
player_height,player_width=24,12
#player_rect = pygame.Rect(x, y, width, height)
player_rect=pygame.Rect(player_position_x,player_position_y,player_width,player_height)
player_anm={"Run":Asset_loader("assets/images/Entity/Player/Run.png",32,32).load(),"Jump":Asset_loader("assets/images/Entity/Player/Jump.png",32,32).load(),
            "Hit":Asset_loader("assets/images/Entity/Player/Hit.png",32,32).load(),"Idle":Asset_loader("assets/images/Entity/Player/Idle.png",32,32).load()}
is_jumping=0
gravity=0.5
velocity_x=2
velocity_y=10
current_velocity_y=0
floor_position_x,floor_position_y=0,100
BLUE= (135,206,235)
BROWN= (150 ,75,0)
#print(dir(a),type(a),type(b),type(f),a[1],f["key1"])
pos_x,pos_y=0,0
sky_rect=pygame.Rect(pos_x,pos_y,tile_size,tile_size)
ground_rect=pygame.Rect(pos_x,pos_y,tile_size,tile_size)
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
offset_x,offset_y=10,8
Player_direction=1 #1 stand for facing right
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
    if keys[pygame.K_LEFT]:
        player_rect.x=player_rect.x-velocity_x
        Player_current_state="Run"
        Player_direction = -1
    if keys[pygame.K_RIGHT]:
        player_rect.x=player_rect.x+velocity_x
        Player_current_state="Run"
        Player_direction =1
    
    for x in range(len(level_map)):
        for y in range(len(level_map[x])):
            tile_type=level_map[x][y] #remember this is how we can use 2D array
            if tile_type==0:
                sky_rect.x,sky_rect.y=y*tile_size,x*tile_size
                pygame.draw.rect(screen,BLUE,sky_rect)
            else:
                ground_rect.x,ground_rect.y=y*tile_size,x*tile_size
                pygame.draw.rect(screen,BROWN,ground_rect)
                if player_rect.colliderect(ground_rect):
                    if current_velocity_y>0:
                        player_rect.bottom=ground_rect.top
                        current_velocity_y=0
                        is_jumping=0
                        #Player_current_state="Idle"


    
    current_velocity_y+=gravity

    #print(current_velocity_y)
    player_rect.y +=  current_velocity_y
    if player_rect.right>=160*2:
        player_rect.right=160*2
    if player_rect.left <=0:
        player_rect.left=0
    if player_rect.top <=0:
        player_rect.top=0

    '''
    #if player is in air apply gravity
    if player_rect.bottom<floor_position_y or current_velocity_y<0:
        current_velocity_y+=gravity
        print(current_velocity_y)
    else:
        player_rect.bottom=floor_position_y
        current_velocity_y=0
        is_jumping =0
       
    if player_rect.bottom >= floor_position_y:
        player_rect.bottom=floor_position_y
        current_velocity_y=0
        is_jumping=0
    '''

                
                
    
    #screen.fill((255,0,0))
   # for x in level_map:
   #     for y in x:
   #         if y==0:
    #            print("0")
     #       else:
      #          print("1")
    
    frames=player_anm[Player_current_state]
    index=int(frame_index)%len(frames)
    current_ann=player_anm[Player_current_state]
    image_draw=current =current_ann[int(frame_index)%len(current_ann)]
    #pygame.draw.rect(screen,(255,255,0),player_rect)
    if Player_direction ==-1:
        image_draw=pygame.transform.flip(image_draw,True,False)
    screen.blit(image_draw,(player_rect.x -offset_x,player_rect.y-offset_y))
    #screen.blit(frames[index],(player_rect.x ,player_rect.y))
    frame_index += 0.15
    pygame.display.flip()
    
    clock.tick(60)

pygame.display.update()