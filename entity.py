
import pygame
import settings
# enemy is like character but it will not jump and shoot. it will keep moving in one direction till collision_x
class Entity():
    def __init__(self,pos_x,pos_y,width,height):
        self.Rect=pygame.Rect(pos_x,pos_y,width,height)
        self.current_speed_y=0
        self.is_on_ground=False
        self.direction =0
        self.is_alive=True
    
    def apply_gravity(self,gravity):
        self.current_speed_y += gravity
        self.Rect.y +=int(self.current_speed_y)
    
    
    def check_collision_x(self,lst):
        for items in lst:
            check_Rect= pygame.Rect(items)
            if self.Rect.colliderect(check_Rect): #returns true or false
                if self.Rect.centerx < check_Rect.centerx:
                    self.Rect.right=check_Rect.left
                else:
                    self.Rect.left=check_Rect.right
    def check_collision_y(self,lst):
        for items in lst:
            check_Rect=pygame.Rect(items)
            #if self.Rect.inflate(-4,0).colliderect(check_Rect):
            if self.Rect.colliderect(check_Rect):
                if self.current_speed_y > 0: #falling
                    self.Rect.bottom=check_Rect.top
                    self.current_speed_y=0
                    self.is_on_ground=True
                elif self.current_speed_y < 0 :
                    self.Rect.top=check_Rect.bottom
                    self.current_speed_y=0
    
    def move_x(self,dx,speed_x):
        self.Rect.x += (dx*speed_x)
        if dx >0:
            self.facing=1
        elif dx<0:
            self.facing=-1

         
        
                    
    def update(self,lst,dx,gravity,speed_x):
        self.is_on_ground=False
        self.move_x(dx,speed_x)
        self.check_collision_x(lst)
        self.apply_gravity(gravity)
        self.check_collision_y(lst)
        if self.is_on_ground:
            self.current_speed_y=0
            
        
    def draw(self,surface,color):
        pygame.draw.rect(surface,color,self.Rect)
        