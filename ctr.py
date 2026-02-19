import pygame
import settings
from entity import Entity
class Character(Entity):
    '''this is test comment '''
    def __init__(self,pos_x,pos_y,width,height):
        super().__init__(pos_x,pos_y,width,height)
        self.is_jumping=True
        self.facing=1
        

        
    def apply_bound(self):
       if self.Rect.left <=0:
           self.Rect.left=0
       if self.Rect.right>=settings.WIDTH:
           self.Rect.right=settings.WIDTH
       if self .Rect.top<=0:
           self.Rect.top=0
       if self.Rect.bottom>=settings.HEIGHT:
           self.Rect.bottom=settings.HEIGHT

                    
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

     
    def move_y(self,dy):
        self.Rect.y += dy*settings.PLAYER_SPEED_Y
    
    def update(self,lst,dx,gravity,speed_x):
        #self.jump()
        self.is_on_ground=False
        self.move_x(dx,speed_x)
        #self.Rect.x += dx*settings.PLAYER_SPEED_X
        self.check_collision_x(lst) 
        #self.move_y()
        self.apply_gravity(gravity)
        
        self.check_collision_y(lst)
        
        if self.is_on_ground:
            self.current_speed_y=0
            self.is_jumping =False
        self.apply_bound()
        
        
    
    def draw(self,surface,color):
        pygame.draw.rect(surface,color,self.Rect)
    

