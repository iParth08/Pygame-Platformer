import random
import math
import pygame
import os
from os import listdir
from os.path import isfile, join


# Global variables
'''BG_COLOR = (255, 255, 255)''' # Why a tupple is used ?
WIDTH, HEIGHT = 1000, 650
FPS = 60

PLAYER_VEL = 5

# pygame setup
pygame.init()
pygame.display.set_caption("Mr Platformer")
window = pygame.display.set_mode((WIDTH, HEIGHT))



# Player Class
class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0) # Red player block

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = 'left'
        self.animation_count = 0

    def move(self, dx, dy):
        self.x_vel += dx
        self.y_vel += dy

    def move_left(self, vel):
        self.x_vel = -vel
        
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0


    def move_right(self, vel):
        self.x_vel = vel

        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0


    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)


# Helper functions
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

def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)

    player.draw(window)
    pygame.display.update() # Clear and repaint

# GAME MASTER CONSOLE
def main(window):
    
    clock = pygame.time.Clock()
    background, bg_image = get_background("Pink.png")

    player = Player(100, 100, 50, 50)

    run = True
    while run:
        clock.tick(FPS) # Ensure max 60 fps
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(window, background, bg_image, player)
        
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)

