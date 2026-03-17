

import pygame
import sys


pygame.init()

screen=pygame.display.set_mode((160,128))
pygame.display.set_caption("game_name")


BLUE=(135,206,235)

screen.fill(BLUE)
clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
    clock.tick(60)
        

