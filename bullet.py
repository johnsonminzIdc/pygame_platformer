import pygame
import settings

class Bullet:
    def __init__(self,pos_x,pos_y,bullet_speed,direction,color):
        self.Rect=pygame.Rect(pos_x,pos_y,settings.BULLET_SIZE,settings.BULLET_SIZE)
        self.color=color
        self.direction=direction
        self.active=True
        self.speed=bullet_speed
    
    
    def check_collision(self,tile_lst):
        if self.Rect.x<0 or self.Rect.x>settings.WIDTH:
            self.active=False
            return
        for tile in tile_lst:
            if self.Rect.colliderect(tile):
                self.active=False
                break
        
    def update(self,tile_lst):
        if self.active == True:
            self.Rect.x += self.speed*self.direction
            self.check_collision(tile_lst)
    
    
    def draw(self,surface):
        if self.active ==True:
            pygame.draw.rect(surface,self.color,self.Rect)
        
        



#print("hello")