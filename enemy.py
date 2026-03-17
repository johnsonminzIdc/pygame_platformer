from entity import Entity
import settings
import pygame
from assetManager import AssetManager

class Enemy1(Entity):
    def __init__(self,pos_x,pos_y,width,height,speed):
        super().__init__(pos_x,pos_y,width,height)
        self.facing=1
        self.direction=1 #can be 1,-1
        self.speed=speed
        self.animation=AssetManager.load("assets/images/Entity/NinjaFrog/Run.png",12)
        self.animation_speed=0.25
        self.frame_index=0
        self.is_alive=True
        
    #i want to create a logic where enemy is spawn at x,y and moves in -x direction , if it collide in x axis it changes it direction
        # or bounding window
    
    def check_collision_x(self,lst):
        old_x=self.Rect.x
        super().check_collision_x(lst)
        if old_x != self.Rect.x:  #collsion x has happen
            self.direction *= -1
            self.facing=self.direction
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animation):
            self.frame_index=0
        self.current_image=self.animation[int(self.frame_index)]
        if self.direction == -1:
            self.current_image=pygame.transform.flip(self.current_image,True,False)
        
    
    def update(self,lst):
        self.is_on_ground=False
        self.move_x(self.direction,self.speed)
        self.check_collision_x(lst)
        self.apply_gravity(settings.GRAVITY)
        self.check_collision_y(lst)
        self.animate()
    
    def draw(self,surface):
        surface.blit(self.current_image,(self.Rect.x,self.Rect.y))
        
    
class Enemy2(Entity):
    def __init__(self,pos_x,pos_y,width,height,speed):
        super().__init__(pos_x,pos_y,width,height)
        self.facing=1
        self.direction=1
        self.speed=speed
        self.animation=AssetManager.load("assets/images/Entity/MaskDude/Run.png",12)
        self.frame_index=0
        self.animation_speed=0.2
        self.is_alive=True
        
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
               
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animation):
            self.frame_index=0
        self.current_image=self.animation[int(self.frame_index)]
        if self.direction == -1:
            self.current_image=pygame.transform.flip(self.current_image,True,False)
        
            
        
    def update(self,lst):
              self.is_on_ground=False
              self.move_x(self.direction,self.speed)
              self.check_collision_x(lst)
              self.check_cliff(lst)
              self.apply_gravity(settings.GRAVITY)
              self.check_collision_y(lst)
              self.animate()
    
    def draw(self,surface):
        #surface.blit(self.current_image,(self.Rect.x-12,self.Rect.y-12))
        surface.blit(self.current_image,(self.Rect.x,self.Rect.y))
        
class Hazzard1(Entity):
    def __init__(self,x_pos,y_pos,width,height):
        super().__init__(x_pos,y_pos,width,height)
        self.animation=AssetManager.load("assets/images/Traps/Fire/On.png",3)
        self.frame_index=0
        self.animation_speed=0.2
        self.is_alive=True
            
            
    def animate(self):
        self.frame_index +=self.animation_speed
        if self.frame_index >= len(self.animation):
            self.frame_index=0
        self.current_image=self.animation[int(self.frame_index)]
        
    def update(self,lst):
        #self.check_collision_X(lst)
        #self.check_collision_y(lst)
        self.animate()
    def draw(self,surface):
        surface.blit(self.current_image,(self.Rect.x,self.Rect.y))

class Hazzard2(Entity):
    def __init__(self,x_pos,y_pos,width,height):
        super().__init__(x_pos,y_pos,width,height)
        #self.is_alive=True
    
    def update(self,lst):
        None
        
    def draw(self,surface):
        current_image=AssetManager.load("assets/images/Traps/Spikes/Idle.png",1)
        show_image=current_image[0]
        surface.blit(show_image,(self.Rect.x,self.Rect.y))
        
class Hazzard3(Entity):
    def __init__(self,x_pos,y_pos,width,height):
        super().__init__(x_pos,y_pos,width,height)
        self.is_alive=True
        self.animation=AssetManager.load("assets/images/Traps/SpikeHead/Blink.png",4)
        self.frame_index=0
        self.animation_speed=0.2
        self.direction=1
        #self.current_pos=0
        self.start_x=x_pos
        self.end_x=x_pos+100
        
    def shoot(self,enemy_bullet_list):
        from bullet import Bullet
        spawn_x=self.Rect.centerx + self.direction*5
        new_enemy_bullet=Bullet(spawn_x,self.Rect.centery,settings.BULLET_SPEED,self.direction,settings.YELLOW)
        enemy_bullet_list.append(new_enemy_bullet)
        
        
        
        
        
        
    def move_x(self):
    
        #if self.current_pos>=self.max_dis or self.current_pos<=0:
        #    self.direction *= -1
        self.Rect.x +=self.direction 
        #self.Rect.x += self.current_pos
        if self.Rect.x <= self.start_x:
            self.direction *= -1
        if self.Rect.x >= self.end_x:
            self.direction *= -1
         
    def animate(self):
        self.frame_index +=self.animation_speed
        if self.frame_index >= len(self.animation):
            self.frame_index=0
        self.current_image=self.animation[int(self.frame_index)]
        
        
    def update(self,lst):
        self.move_x()
        self.animate()
    
    def draw(self,surface):
        surface.blit(self.current_image,(self.Rect.x,self.Rect.y))
    
class Platform1(Entity):
    def __init__(self,pos_x,pos_y,weigth,height,range_x,speed,):
        super().__init__(pos_x,pos_y,weigth,height)
        #Brown On (32x8).png ,Grey On (32x8).png 
        self.animation=AssetManager.load("assets/images/Traps/Platforms/BrownOn.png",8)
        self.frame_index=0
        self.animation_speed=.2
        self.direction=-1
        self.speed=speed
        self.start_x=pos_x
        self.range_x=range_x
        self.end_x=pos_x + range_x
        
        self.change_x=0
        self.change_y=0
        
        
    def move_x(self):
        old_x,old_y=self.Rect.x,self.Rect.y
        self.Rect.x += self.direction*self.speed
        if self.direction == 1 and self.Rect.x >=self.end_x:
            self.Rect.x = self.end_x
            self.direction = -1
        elif self.direction==-1 and self.Rect.x <=self.start_x:
            self.Rect.x=self.start_x
            self.direction = 1
        self.change_x=self.Rect.x-old_x
        self.change_y=self.Rect.y-old_y
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animation):
            self.frame_index=0
        self.current_frame=self.animation[int(self.frame_index)]
        
        
    def update(self,lst):
        self.move_x()
        self.animate()
        
    def draw(self,surface):
        surface.blit(self.current_frame,(self.Rect.x,self.Rect.y))
    
    
        
        
            
            

            
        
        
        