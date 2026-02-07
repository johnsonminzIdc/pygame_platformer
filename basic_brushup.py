import pygame
import sys

pygame.init()
screen=pygame.display.set_mode((160,128))
pygame.display.set_caption("map")
#print("hello world")
tile_size=16
#a=[5,6,7,8]
#b=(5,6,7)
#f={"key1":"johnson","key2":"hohnson"}
BLUE= (135,206,235)
BROWN= (150 ,75,0)
#print(dir(a),type(a),type(b),type(f),a[1],f["key1"])
pos_x,pos_y=0,0
sky_rect=pygame.Rect(pos_x,pos_y,tile_size,tile_size)
ground_rect=pygame.Rect(pos_x,pos_y,tile_size,tile_size)

level_map=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,0,1,1],
    ]
#for x in range(len(level_map)):
#    for y in range(len(level_map[x])):
#        if y==0:
#            print("sky",x,y)
#        else:
#            print("ground",x,y)
clock=pygame.time.Clock()  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill((0,0,255))
    #pygame.draw.rect(screen,BLUE,sky_rect)
    for x in range(len(level_map)):
        for y in range(len(level_map[x])):
            tile_type=level_map[x][y] #remember this is how we can use 2D array
            if tile_type==0:
                sky_rect.x,sky_rect.y=y*tile_size,x*tile_size
                pygame.draw.rect(screen,BLUE,sky_rect)
            else:
                ground_rect.x,ground_rect.y=y*tile_size,x*tile_size
                pygame.draw.rect(screen,BROWN,ground_rect)


                #print("ground",x,y)
    pygame.display.flip()
    clock.tick(60)
    
        
    
