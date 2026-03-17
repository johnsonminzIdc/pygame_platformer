import pygame

class AssetManager:
    @staticmethod
    def load(path,frame_count):
        sheet=pygame.image.load(path).convert_alpha()
        sheet_rect=sheet.get_rect()
        frame_width=sheet_rect.width // frame_count
        frame_height=sheet_rect.height
        frames=[]
        for x in range(0,sheet_rect.width,frame_width):
            cut_rect=pygame.Rect(x,0,frame_width,frame_height)
            frame=sheet.subsurface(cut_rect)
            frames.append(frame)
        return frames
            
            
        
    
    