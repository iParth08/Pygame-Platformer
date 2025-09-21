### FILE: src/player.py
"""
Player class focuses on player state, physics, and animation.
It accepts an input handler and does not read pygame events directly (DIP).
"""
import pygame
from utils import load_sprite_sheets
from config import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_GRAVITY, MAX_DOUBLE_JUMP


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width=PLAYER_WIDTH, height=PLAYER_HEIGHT):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = 'left'
        self.animation_count = 0
        self.fall_time = 0
        self.jump_count = 0
        self.hit_state = False
        self.hit_state_time = 0

        # animation placeholders
        self.SPRITES = load_sprite_sheets('MainCharacters', 'MaskDude', 32, 32, True)
        self.ANIMATION_DELAY = 3
        self.sprite = pygame.Surface((width, height), pygame.SRCALPHA)

    # --- Movement and physics (SRP: player handles physics & movement only)
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def set_velocity(self, vx, vy):
        self.x_vel = vx
        self.y_vel = vy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != 'left':
            self.direction = 'left'
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != 'right':
            self.direction = 'right'
            self.animation_count = 0

    def jump(self):
        if self.jump_count < MAX_DOUBLE_JUMP:
            if self.jump_count == 1:
                self.y_vel = -PLAYER_GRAVITY * 10
            else:
                self.y_vel = -PLAYER_GRAVITY * 8
            self.animation_count = 0
            self.jump_count += 1
            if self.jump_count == 1:
                self.fall_time = 0

    def hit(self):
        self.hit_state = True
        self.hit_state_time = 0

    def landed(self):
        self.fall_time = 0
        self.jump_count = 0
        self.y_vel = 0

    def hit_head(self):
        self.y_vel *= -1
        self.count = 0

    def loop(self, fps):
        # basic gravity integration
        self.y_vel += min(1, (self.fall_time / max(1, fps) * PLAYER_GRAVITY))
        self.move(self.x_vel, self.y_vel)
        self.fall_time += 1

        if self.hit_state:
            self.hit_state_time += 1
        if self.hit_state_time > fps * 2:
            self.hit_state = False

        self.update_sprite()

    def update_sprite(self):
        sprite_sheet = 'idle'
        if self.hit_state:
            sprite_sheet = 'hit'
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = 'jump'
            elif self.jump_count == 2:
                sprite_sheet = 'double_jump'
        elif self.y_vel > PLAYER_GRAVITY * 2:
            sprite_sheet = 'fall'
        elif self.x_vel != 0:
            sprite_sheet = 'run'

        sprite_sheet_name = sprite_sheet + '_' + self.direction
        sprites = self.SPRITES.get(sprite_sheet_name)
        if sprites:
            sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
            self.sprite = sprites[sprite_index]
            self.animation_count += 1
        # fallback: keep rect size
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, surface, offset_x=0, offset_y=0):
        surface.blit(self.sprite, (self.rect.x - offset_x, self.rect.y-offset_y))
