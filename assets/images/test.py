import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((200,200))
clock=pygame.time.Clock()


frame1=pygame.image.load("run_1.png").convert_alpha()
frame2=pygame.image.load("run_2.png").convert_alpha()
frame3=pygame.image.load("run_3.png").convert_alpha()
frame4=pygame.image.load("run_4.png").convert_alpha()
frame5=pygame.image.load("run_5.png").convert_alpha()
frame6=pygame.image.load("run_6.png").convert_alpha()
frame7=pygame.image.load("run_7.png").convert_alpha()
frame8=pygame.image.load("run_8.png").convert_alpha()
frame9=pygame.image.load("run_9.png").convert_alpha()
frame10=pygame.image.load("run_10.png").convert_alpha()
frame11=pygame.image.load("run_11.png").convert_alpha()
frame12=pygame.image.load("run_12.png").convert_alpha()
#loading  the enemy sheet by .load --convert_alpha() method
frame_sheet=pygame.image.load("Enemy_Run.png").convert_alpha()
# ???
enemy_sheet_rect=frame_sheet.get_rect()
#create empty list of frame
enemy_frame=[]
#slicing dimention
frame_width=32
frame_height=32
#loading frame from sprite sheet
for x in range(0,enemy_sheet_rect.width,32): # from zero to total width let say 384 in this case ,step size 32
   # Rect arguments are: (left, top, width, height)
    cut_rect=pygame.Rect(x,0,frame_width,frame_height)
 #Use the IMAGE (frame_sheet) create a subsurface out of frame_sheet of rect of dimension cut_Rect 
    enemy_frames=frame_sheet.subsurface(cut_rect)
    enemy_frame.append(enemy_frames)
#now we have enemey_frame loaded up

walk_frame=[frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8,frame9,frame10,frame11,frame12]

current_frame=0
enemy_current_frame=0
animation_speed=0.5
enemy_animation_speed=0.8
x_pos=0
enemy_speed=1
player_speed=1
direction=1

while True:
    # --- STEP 2: EVENT HANDLING ---
    event_list=pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            sys.exit()
    # --- STEP 3: LOGIC ---
    current_frame += animation_speed
    enemy_current_frame += enemy_animation_speed
    if enemy_current_frame >=len(enemy_frame):
        enemy_current_frame=0
    if current_frame>= len(walk_frame):
        current_frame=0
        # --- STEP 4: DRAWING ---
    screen.fill((255, 255, 255))

    active_image=walk_frame[int(current_frame)]
    active_image_enemy=enemy_frame[int(enemy_current_frame)]
    if direction == -1:
        active_image = pygame.transform.flip(active_image, True, False)
        active_image_enemy=pygame.transform.flip(active_image_enemy,True,False)
    screen.blit(active_image,(x_pos,100))
    screen.blit(active_image_enemy,(x_pos-32,100))
    x_pos +=player_speed*direction
    if x_pos>=200-16 or x_pos<=-16:
        direction *= -1
    pygame.display.update()
    clock.tick(60)
