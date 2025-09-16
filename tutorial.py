import random
import math
import pygame
import os
from os import listdir
from os.path import isfile, join


# Global variables
BG_COLOR = (255, 255, 255) # Why a tupple is used ?
WIDTH, HEIGHT = 1000, 650
FPS = 60

PLAYER_VEL = 5

# pygame setup
pygame.init()
pygame.display.set_caption("Mr Platformer")
window = pygame.display.set_mode((WIDTH, HEIGHT))

# functions
def main(window):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS) # Ensure max 60 fps
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)

