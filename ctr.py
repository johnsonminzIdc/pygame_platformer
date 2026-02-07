import pygame
import settings

class Character:
    def __init__(self,pos_x,pos_y,width,height):
        self.Rect=pygame.Rect(pos_x,pos_y,width,height)
        self.current_speed_y=0
        self.is_jumping=True
        self.facing=1
        
        
    def apply_gravity(self):
        self.current_speed_y += settings.GRAVITY
        self.Rect.y += self.current_speed_y
        
    def apply_bound(self):
       if self.Rect.left <=0:
           self.Rect.left=0
       if self.Rect.right>=settings.WIDTH:
           self.Rect.right=settings.WIDTH
       if self .Rect.top<=0:
           self.Rect.top=0
       if self.Rect.bottom>=settings.HIGHT:
           self.Rect.bottom=settings.HIGHT
    
    def check_collision(self,lst):
        for items in lst:
            check_Rect=pygame.Rect(items)
            if self.Rect.colliderect(check_Rect):
                if self.current_speed_y>0:
                    self.Rect.bottom=check_Rect.top
                    self.current_speed_y=0
                    self.is_jumping=False
    #jump logic can be made by checking if player is ground and pressed spacebar then current_speed_y = jump_speed -gravity
                    
    def jump(self,jump_trigger):
        if jump_trigger ==1 and self.is_jumping == False:
            self.is_jumping=True
            self.current_speed_y = -settings.JUMP_SPEED
    
    #def can_attack():
        
    def shoot(self,can_shoot,DIRECTION,bullet_lst):
        if can_shoot:
            from bullet import Bullet #Local import to circular
            spwan_x=self.Rect.centerx +(DIRECTION*5) #player dont shot itself
            new_bullet=Bullet(spwan_x,self.Rect.y,settings.BULLET_SPEED,DIRECTION,settings.YELLOW)
            #inject in the shared list 
            bullet_lst.append(new_bullet)
            #self.cooldown=20
            
            
    
    #attack logic is swaning point in x direction / or in key direction like contra
    def move(self,dx,dy):
        self.Rect.x += dx*settings.PLAYER_SPEED_X
        self.Rect.y += dy*settings.PLAYER_SPEED_Y
        if dx>0:
            self.facing=1
        elif dx<0:
            self.facing=-1
    
    def update(self,lst):
        #self.jump(jump_trigger)
        self.check_collision(lst)
        self.apply_bound()
        self.apply_gravity()
        
    
    def draw(self,surface,color):
        pygame.draw.rect(surface,color,self.Rect)
    
    
#   
