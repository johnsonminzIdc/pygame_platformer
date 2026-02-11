from entity import Entity
import settings
import pygame

class Enemy(Entity):
    def __init__(self,	pos_x,pos_y,width,height,speed):
        super().__init__(pos_x,pos_y,width,height)
        self.facing=1
        self.direction=1 #can be 1,-1
        self.speed=speed
        
    #i want to create a logic where enemy is spawn at x,y and moves in -x direction , if it collide in x axis it changes it direction
        # or bounding window 
    #overridding method check collision x
    #def check_collision_x(self,lst):
    #    for items in lst:
    #        check_Rect=pygame.Rect(items)
    #        if self.Rect.colliderect(check_Rect):
    #            self.direction *= -1
    ##            if self.Rect.centerx<check_Rect.centerx:
    #                self.Rect.right=check_Rect.left
    #            else:
    #                self.Rect.left = check_Rect.right
    #def update(self,lst,direction,gravity,speed_x):
    
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

            
        
        
        