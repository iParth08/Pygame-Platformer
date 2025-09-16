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
def get_background(color_name):
    image = pygame.image.load(join("assets", "Background", color_name))
    _, _, width, height = image.get_rect()

    tiles = []
    # marking locations (coords) for image/tile placement
    for i in range(WIDTH //width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i*width, j*height)
            tiles.append(pos)
        
    return tiles, image
def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

    pygame.display.update() # Clear and repaint
def main(window):
    
    clock = pygame.time.Clock()
    background, bg_image = get_background("Pink.png")

    run = True
    while run:
        clock.tick(FPS) # Ensure max 60 fps
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(window, background, bg_image)
        
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)

