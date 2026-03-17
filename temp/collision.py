'''new_list=[
    [[2,5,6],[2,5,6],[2,9,6]],
    [[6,5,3],[2,9,6],[2,5,6]],
    [[5,7,8],[2,5,6],[2,5,6]],
    ]
print(new_list[0][0][0])
#for x in new_list:
#    for y in x:
#        print(y) '''

import pygame
import sys


pygame.init()

screen=pygame.display.set_mode((160,128))
pygame.display.set_caption("collison")

tile_size=16

map=[
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,0,1,1],
    ]

BLUE=(135,206,235)
BROWN=(150,75,0)
RED=(255,0,0)
ground_tile=pygame.Rect(0,0,tile_size,tile_size)
box=pygame.Rect(20,0,20,20)
dy=5
screen.fill(BLUE)
clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(BLUE)
    box.y += dy
    for row in range(len(map)):
        for col in range(len(map[row])):
            
            if map[row][col]==1:
                ground_tile.x,ground_tile.y=col*tile_size,row*tile_size
                pygame.draw.rect(screen,BROWN,ground_tile)
            if box.colliderect(ground_tile):
                box.bottom=ground_tile.top
                       
    
    #if box.colliderect(ground_tile):
    #    dx=0
    pygame.draw.rect(screen,RED,box)
    pygame.display.flip()
    clock.tick(60)
        
