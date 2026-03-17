import pygame

class Asset_loader:
    def __init__ (self,name,frame_width,frame_height):
        self.frame_width=frame_width
        self.frame_height=frame_height
        self.name=name
        
    
    def load(self):
        sheet=pygame.image.load(self.name).convert_alpha()
        sheet_rect=sheet.get_rect()
        frames=[]
        for x in range(0,sheet_rect.width,self.frame_width):
            cut_rect=pygame.Rect(x,0,self.frame_width,self.frame_height)
            frame=sheet.subsurface(cut_rect)
            frames.append(frame)
        return frames
            
            
        
    
    