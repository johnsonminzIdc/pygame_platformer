import pygame

def check_movements(dx,dy):
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dx = -1
        #print("going left")
    if keys[pygame.K_RIGHT]:
        dx=1
        #print("going right")
    if keys[pygame.K_UP]:
        dy= -1
        #print("going up")
    if keys[pygame.K_DOWN]:
        dy= 1
        #print("going down")
    return dx,dy
    
def check_actions(is_jumping,is_attacking):
    jump_trigger=False
    attack_trigger=False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping :
                #jump_trigger=True
                print("is attacking")
            if event.key == pygame.K_v and not is_attacking:
                attack_trigger=True
                #print("is jumping")
    return jump_trigger, attack_trigger


