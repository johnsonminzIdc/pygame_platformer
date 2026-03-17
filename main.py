import pygame
import settings
import world
import sys
import ip_handle
from enemy import Enemy1
from enemy import Enemy2
from enemy import Hazzard1
from enemy import Hazzard2,Hazzard3,Platform1
from ctr import Character


pygame.init()
screen=pygame.display.set_mode((settings.WIDTH*settings.SCALE,settings.HEIGHT*settings.SCALE))
canvas=pygame.Surface((settings.WIDTH,settings.HEIGHT)).convert()
pygame.display.set_caption("johnson")

clock=pygame.time.Clock()
tile_image=pygame.image.load("assets/images/Terrain/Terrain.png").convert_alpha()

player=Character(200,8,settings.PLAYER_WIDTH,settings.PLAYER_HEIGHT)
tile_lst=world.get_tile_rects(settings.LEVEL_MAP)
player_bullet=[]
enemy_bullet=[]

enemy1=Enemy1(12,0,settings.ENEMY_WIDTH,settings.ENEMY_HIGHT,settings.ENEMY_SPEED)
enemy2=Enemy2(120,0,settings.ENEMY_WIDTH,settings.ENEMY_HIGHT,settings.ENEMY_SPEED)
spike=Hazzard2(64,16,16,32)
fire1=Hazzard1(32,16,16,32)
spikehead=Hazzard3(64,16,54,52)
platform1=Platform1(64,150,32,8,150,settings.PF_SPEED)
enemies=[enemy1,enemy2,fire1,spike,spikehead]
platforms=[platform1]

while True:
    active_enemy=[]
    event_list=pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            sys.exit()
    
    #2) clear Screen(wipe the old frame)
    canvas.fill(settings.BLUE)
    # 1) handle inputs (what does player want to do)
    user_move=ip_handle.user_intent(event_list)
    # 2) update physics (gravity walking,enemy ai movement)
    player.jump(user_move["jump"])
    player.direction=user_move["x-axis"]
    player.shoot(user_move["attack"],player.facing,player_bullet)
    player.update(tile_lst,player.direction,settings.GRAVITY,settings.PLAYER_SPEED_X)
    #print(player.facing)
    #3)#Resolve collision (did they hit a wall? did enemy touch the player?)
    #enemy1.update(tile_lst)
    #enemy2.update(tile_lst)
    for pf in platforms:
        pf.update(tile_lst)
        if pf.Rect.inflate(0,2).colliderect(player.Rect):
            if player.Rect.bottom<=pf.Rect.top+5 and player.current_speed_y >=0:
                player.Rect.x += pf.change_x
                player.Rect.bottom = pf.Rect.top
                player.current_speed_y=0
                player.is_jumping= False
                player.is_on_ground=True
        
    for bullet in player_bullet:
        bullet.update(tile_lst)
    alive_bullet=[]
    for bullet in player_bullet:
        if bullet.active:
            alive_bullet.append(bullet)
    player_bullet=alive_bullet
    for  enemy in enemies:
        enemy.update(tile_lst)
        if player.Rect.colliderect(enemy.Rect) and enemy.is_alive:
            player.is_alive=False
            #.active=False
        for bullet in player_bullet:
            if enemy.Rect.colliderect(bullet.Rect) and enemy.is_alive:
                #if enemy == fire1 or spike :break make hazzards invincible
                enemy.is_alive=False
                bullet.active=False
    
    for bullet in enemy_bullet:
        bullet.update(tile_lst)
        
    enemy_alive_bullet=[]
    for bullet in enemy_bullet:
        if bullet.active:
            enemy_alive_bullet.append(bullet)
    enemy_bullet=enemy_alive_bullet
    for enemy in enemies:
        if enemy.is_alive:
            active_enemy.append(enemy)
    enemies=active_enemy
    
    #enemy bullet
    if player.Rect.bottom <=spikehead.Rect.bottom and player.Rect.top>=spikehead.Rect.top :
       spikehead.shoot(enemy_bullet)
    for bullet in enemy_bullet:
        if player.Rect.colliderect(bullet.Rect) and player.is_alive:
            player.is_alive=False
            bullet.active=False
    
    
    #4) Render(draw the map, then the characters)
    world.draw_map(settings.LEVEL_MAP,tile_image,settings.BLUE,canvas)
    for pf in platforms:
        pf.draw(canvas)
    if player.is_alive:
        player.draw(canvas)
    for enemy in enemies:
        enemy.draw(canvas)
    #enemy1.draw(canvas)
    #enemy2.draw(canvas)
    for bullet in player_bullet:
        bullet.draw(canvas)
    for bullet in enemy_bullet:
        bullet.draw(canvas)
    scaled_canvas=pygame.transform.scale_by(canvas,settings.SCALE)
    screen.blit(scaled_canvas,(0,0))


   #5) display FLiip and Tick(Show it t the user and wait)

    pygame.display.flip()
    clock.tick(60)
#pygame.display.update()



