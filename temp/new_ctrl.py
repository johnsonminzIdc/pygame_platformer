import pygame
import settings
from entity import Entity
class Character():
    def __init__(self,pos_x,pos_y,width,height):
        self.Rect=pygame.Rect(pos_x,pos_y,width,height)
        self.current_speed_y=0
        self.is_jumping=True
        self.facing=1
        self.is_on_ground=False
        
        
    def apply_gravity(self):
        self.current_speed_y += settings.GRAVITY
        self.Rect.y += int(self.current_speed_y)
        
    def apply_bound(self):
       if self.Rect.left <=0:
           self.Rect.left=0
       if self.Rect.right>=settings.WIDTH:
           self.Rect.right=settings.WIDTH
       if self .Rect.top<=0:
           self.Rect.top=0
       if self.Rect.bottom>=settings.HEIGHT:
           self.Rect.bottom=settings.HEIGHT

    def check_collision_x(self, lst):
        for items in lst:
            check_rect = pygame.Rect(items)
            if self.Rect.colliderect(check_rect):
                # Use position relative to the block to decide which way to push
                if self.Rect.centerx < check_rect.centerx:
                    self.Rect.right = check_rect.left
                else:
                    self.Rect.left = check_rect.right                
    
    
    
    
    
    '''def check_collision_x(self,lst):
        for items in lst:
            check_rect=pygame.Rect(items)
            if self.Rect.inflate(0,-8).colliderect(check_rect.inflate(0,-4)):
                vertical_gap = check_rect.top - self.Rect.bottom

             # If platform is below us, ignore horizontal collision coyote margin
                if vertical_gap > -4:
                    continue
                if self.facing >0 :
                    self.Rect.right=check_rect.left    
                elif self.facing <0 :
                    self.Rect.left=check_rect.right'''
    
                        
    def check_collision_y(self,lst):
        
        for items in lst:
            check_rect=pygame.Rect(items)
            if self.Rect.inflate(-4,0).colliderect(check_rect):
                if self.current_speed_y>0: #falling down              
                    self.Rect.bottom=check_rect.top
                    self.is_jumping=False
                    self.is_on_ground=True
                    self.current_speed_y=0
                elif self.current_speed_y<0: #jumping up head hit
                    self.Rect.top=check_rect.bottom
                    self.current_speed_y=0
    #jump logic can be made by checking if player is ground and pressed spacebar then current_speed_y = jump_speed -gravity
                    
    def jump(self,jump_trigger):
        if jump_trigger ==1 and self.is_jumping == False:
            self.is_jumping=True
            self.is_on_ground=False
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


    def move_x(self,dx):
        self.Rect.x +=int(dx*settings.PLAYER_SPEED_X)
        if dx>0:
            self.facing=1
        elif dx<0:
            self.facing=-1
            
    def move_y(self,dy):
        self.Rect.y += dy*settings.PLAYER_SPEED_Y
    
    def update(self,lst,dx):
        #self.jump(jump_trigger)
        self.is_on_ground=False
        self.move_x(dx)
        #self.Rect.x += dx*settings.PLAYER_SPEED_X
        self.check_collision_x(lst) 
        #self.move_y()
        self.apply_gravity()
        
        self.check_collision_y(lst)
        
        if self.is_on_ground:
            self.current_speed_y=0
        self.apply_bound()
        
        
    
    def draw(self,surface,color):
        pygame.draw.rect(surface,color,self.Rect)
    
    
#   

