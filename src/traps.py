### FILE: src/traps.py
"""
Trap abstraction and implementations (Fire small example).
Follows OCP: add new trap types by subclassing Trap.
"""
from objects import GameObject
import pygame
from utils import load_sprite_sheets


class Trap(GameObject):
    def __init__(self, x, y, width, height, name='Trap'):
        super().__init__(x, y, width, height, name)

    def is_dangerous(self):
        return True

    def loop(self, dt):
        """Optional updating method for animated traps."""
        pass


class Fire(Trap):
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, 'Fire')
        self.sprites = load_sprite_sheets('Traps', 'Fire', width, height)
        # expected keys: 'off', 'on'
        # safe fallback
        key = list(self.sprites.keys())[0] if self.sprites else None
        if key:
            self.image = self.sprites[key][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = 'off'

    def on(self):
        self.animation_name = 'on'

    def off(self):
        self.animation_name = 'off'

    def loop(self, dt):
        sprites = self.sprites.get(self.animation_name, [self.image])
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
