import pygame
import settings
import world
import sys
import ip_handle
from ctr import Character


pygame.init()
screen=pygame.display.set_mode((settings.WIDTH*settings.SCALE,settings.HIGHT*settings.SCALE))
canvas=pygame.Surface((settings.WIDTH,settings.HIGHT))
pygame.display.set_caption("johnson")
is_attacking=0
is_jumping=0
dx=0
dy=0
clock=pygame.time.Clock()
#for wld in world.get_tile_rects(settings.LEVEL_MAP):
#    print(wld)
#print(world.get_tile_rects(settings.LEVEL_MAP))
#for i in range(1000):
#    clock.tick(60)
player=Character(16,16,settings.PLAYER_WIDTH,settings.PLAYER_HIGHT)
tile_lst=world.get_tile_rects(settings.LEVEL_MAP)
player_bullet=[]
while True:
    event_list=pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            sys.exit()
    
    
    # 1) handle inputs (what does player want to do)
    user_move=ip_handle.user_intent(event_list)
    #print(user_move)
    #move_direction=  ip_handle.check_actions(dx,dy)
    player.move(user_move["x-axis"],user_move["y-axis"])
    player.jump(user_move["jump"])
    player.shoot(user_move["attack"],player.facing,player_bullet)
    #player.shoot.check_collision(tile_lst)
    # 2) update physics (gravity walking,enemy ai movement)
    player.update(tile_lst)
    
    #world.draw_map(settings.LEVEL_MAP,settings.BLUE,settings.BROWN,canvas)
    for bullet in player_bullet:
        bullet.update(tile_lst)
    #player.shoot.update()
    
    #ip_handle.check_movements(is_jumping,is_attacking)
    alive_bullet=[]
    for bullet in player_bullet:
        if bullet.active:
            alive_bullet.append(bullet)
    player_bullet=alive_bullet
    world.draw_map(settings.LEVEL_MAP,settings.BLUE,settings.BROWN,canvas)
    
    player.draw(canvas,settings.RED)
    for bullet in player_bullet:
        bullet.draw(canvas)
    #player.shoot.draw()
    scaled_canvas=pygame.transform.scale_by(canvas,settings.SCALE)
    screen.blit(scaled_canvas,(0,0))
    pygame.display.flip()
    clock.tick(60)
#pygame.display.update()

#clear Screen(wipe the old frame)
#handle inputs (what does player want to do)
#update physics (gravity walking,enemy ai movement)
#Resolve collision (did they hit a wall? did enemy touch the player?)
#Render(draw the map, then the characters)
#display FLiip and Tick(Show it t the user and wait)

