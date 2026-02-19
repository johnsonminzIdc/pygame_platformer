from entity import Entity
import settings
import pygame

class Enemy1(Entity):
    def __init__(self,pos_x,pos_y,width,height,speed):
        super().__init__(pos_x,pos_y,width,height)
        self.facing=1
        self.direction=1 #can be 1,-1
        self.speed=speed
        
    #i want to create a logic where enemy is spawn at x,y and moves in -x direction , if it collide in x axis it changes it direction
        # or bounding window
    
    def check_collision_x(self,lst):
        old_x=self.Rect.x
        super().check_collision_x(lst)
        if old_x != self.Rect.x:  #collsion x has happen
            self.direction *= -1
            self.facing=self.direction
    
    def update(self,lst):
        self.is_on_ground=False
        self.move_x(self.direction,self.speed)
        self.check_collision_x(lst)
        self.apply_gravity(settings.GRAVITY)
        self.check_collision_y(lst)
    
class Enemy2(Entity):
    def __init__(self,pos_x,pos_y,width,height,speed):
        super().__init__(pos_x,pos_y,width,height)
        self.facing=1
        self.direction=1
        self.speed=speed
        
    def check_collision_x(self,lst):
        old_x=self.Rect.x
        super().check_collision_x(lst)
        if old_x != self.Rect.x:  #collsion x has happen
            self.direction *= -1
            self.facing=self.direction
    
    def check_cliff(self,lst):
        if self.facing < 0:
            sensor_x=self.Rect.left-1
        else:
            sensor_x=self.Rect.right
        found_ground=False
        sensor_Rect=pygame.Rect(sensor_x,self.Rect.bottom+1,1,1)
        
        for item in lst:
            floor_Rect=pygame.Rect(item)
            if sensor_Rect.colliderect(floor_Rect):
                found_ground= True
                break
        if not found_ground:
            self.direction *= -1
            self.facing=self.direction
               
            
            
        
    def update(self,lst):
              self.is_on_ground=False
              self.move_x(self.direction,self.speed)
              self.check_collision_x(lst)
              self.check_cliff(lst)
              self.apply_gravity(settings.GRAVITY)
              self.check_collision_y(lst)
              
            

            
        
        
        