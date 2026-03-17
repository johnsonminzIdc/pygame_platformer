import pygame
import settings
from entity import Entity
from assetManager import AssetManager

class Character(Entity):
    '''this is test comment '''
    def __init__(self,pos_x,pos_y,width,height):
        super().__init__(pos_x,pos_y,width,height)
        self.is_jumping=True
        self.facing=1
        #define animation as a dictonary
        self.animation={
            "run":AssetManager.load("assets/images/Entity/Player/Run.png",12),
            "jump":AssetManager.load("assets/images/Entity/Player/Jump.png",1),
            "idle":AssetManager.load("assets/images/Entity/Player/Idle.png",11)
            
            }
        #animation state we will add index and self animation to get the required animation
        self.status="run"
        self.frame_index =0
        self.animation_speed=0.30
        self.is_alive=True
        
        

        
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
            new_bullet=Bullet(spwan_x,self.Rect.centery,settings.BULLET_SPEED,DIRECTION,settings.YELLOW)
            #inject in the shared list 
            bullet_lst.append(new_bullet)
            #self.cooldown=20      
    
    #attack logic is swaning point in x direction / or in key direction like contra

     
    def move_y(self,dy):
        self.Rect.y += dy*settings.PLAYER_SPEED_Y
    
    
    def animate(self):
        self.frame_index += self.animation_speed
        
        current_frame=self.animation[self.status]
        if self.frame_index >=len(current_frame):
            self.frame_index=0
        
        self.image=current_frame[int(self.frame_index)]
        #if self.direction < 0:
        #    self.image=pygame.transform.flip(self.image,True,False)
    
    def get_status(self):
        old_status=self.status
       ##if self.is_on_ground == False:
       #     self.status = "jump"
        if not self.is_on_ground and abs(self.current_speed_y) > 1:
            self.status = "jump"       
       
        elif self.direction != 0:
            self.status="run"
        else:
            self.status="idle"
        if old_status != self.status:
            self.frame_index=0
            
        
        
    
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
        self.get_status()
        self.animate()
        
        
    
    def draw(self,surface):
        
        #scaled_canvas=pygame.transform.scale(surface,(settings.SCALE*width,Scale*height))
        #draw_image=pygame.transform.scale(self.image,(16,16))
        draw_image=self.image
        if self.facing <0:
            draw_image=pygame.transform.flip(draw_image,True,False)
            
        render_rect=draw_image.get_rect()
        render_rect.midbottom=self.Rect.midbottom
        surface.blit(draw_image,render_rect)
        #pygame.draw.rect(surface,color,self.Rect)
    

