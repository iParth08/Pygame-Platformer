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





# ---------------------------- Helper functions ----------------------------

# Load background as required
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

# Flip sprites when bi-directional required
def flip(sprites):
    # flip a sprite x-axis (horizontally)
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

# Load any kind of sprite
def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [file for file in listdir(path) if isfile(join(path, file))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i*width, 0, width, height)
            surface.blit(sprite_sheet, (0,0), rect)

            sprites.append(pygame.transform.scale2x(surface))
        
        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "") + ""] = sprites
    
    return all_sprites


# Draw on window (Screen)
def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)

    player.draw(window)
    pygame.display.update() # Clear and repaint

# Handle Movement of Players
def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)

# ---------------------------- Classes --------------------------

# Player Class
class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0) # Red player block
    GRAVITY = 1 # 9.8
    SPRITES = load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = 'left'
        self.animation_count = 0
        self.fall_time = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

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
        # How this gravity logic works : Platform needed
        # self.y_vel += min(1, (self.fall_time / fps * self.GRAVITY))
        self.move(self.x_vel, self.y_vel)
        self.fall_time += 1

        self.update_sprite()

    def update_sprite(self):
        sprite_sheet = "idle"

        if self.x_vel != 0:
            sprite_sheet = "run"
        

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)

        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        # handle mask and collision (pixel-perfect), update is overriden here
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, window):
        # pygame.draw.rect(window, self.COLOR, self.rect)
        window.blit(self.sprite, (self.rect.x, self.rect.y))


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

        player.loop(FPS)
        handle_move(player)
        draw(window, background, bg_image, player)
        
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)

