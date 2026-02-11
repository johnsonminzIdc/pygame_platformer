import pygame
import settings
import world
import sys
import ip_handle
from enemy import Enemy
from ctr import Character


pygame.init()
screen=pygame.display.set_mode((settings.WIDTH*settings.SCALE,settings.HEIGHT*settings.SCALE))
canvas=pygame.Surface((settings.WIDTH,settings.HEIGHT)).convert()
pygame.display.set_caption("johnson")
#is_attacking=0
#is_jumping=0
#dx=0
#dy=0
clock=pygame.time.Clock()

player=Character(16,16,settings.PLAYER_WIDTH,settings.PLAYER_HIGHT)
tile_lst=world.get_tile_rects(settings.LEVEL_MAP)
player_bullet=[]
enemy1=Enemy(120,16,10,10,2)


while True:
    event_list=pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            sys.exit()
    
    #2) clear Screen(wipe the old frame)
    # 1) handle inputs (what does player want to do)
    user_move=ip_handle.user_intent(event_list)
    # 2) update physics (gravity walking,enemy ai movement)
    player.jump(user_move["jump"])
    player.shoot(user_move["attack"],player.facing,player_bullet)
    player.update(tile_lst,user_move["x-axis"],settings.GRAVITY,settings.PLAYER_SPEED_X)
    #print(player.facing)
    #3)#Resolve collision (did they hit a wall? did enemy touch the player?)
    enemy1.update(tile_lst)
    for bullet in player_bullet:
        bullet.update(tile_lst)
   
    alive_bullet=[]
    for bullet in player_bullet:
        if bullet.active:
            alive_bullet.append(bullet)
    player_bullet=alive_bullet
    
    
    #4) Render(draw the map, then the characters)
    world.draw_map(settings.LEVEL_MAP,settings.BLUE,settings.BROWN,canvas)
    
    player.draw(canvas,settings.RED)
    enemy1.draw(canvas,(0,0,0))
    for bullet in player_bullet:
        bullet.draw(canvas)
    scaled_canvas=pygame.transform.scale_by(canvas,settings.SCALE)
    screen.blit(scaled_canvas,(0,0))

   #5) display FLiip and Tick(Show it t the user and wait)

    pygame.display.flip()
    clock.tick(60)
#pygame.display.update()



