import pygame
import settings
class Character():
    def __init__(self,x_pos,y_pos,height,width):
        self.height=height
        self.width=width
        self.vel_x=vel_x
        self.vel_y=vel_y
        self.character=pygame.Rect(x_pos,y_pos,width,height)
        
    def move(self,vel_x,vel_y):
        self.character.x +=vel_x
        self.character.y +=vel_y
    
    def jump(self,jump_trigger,in_the_air):
        if jump_trigger and not in_the_air:
            current_vel_y += settings.GRAVITY
            self.character.y += current_vel_y
        
        