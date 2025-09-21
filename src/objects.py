### FILE: src/objects.py
"""
Base object classes (Drawable, Collidable) and simple world objects.
We separate interfaces using abstract base classes to follow ISP.
"""
from abc import ABC, abstractmethod
import pygame


class Drawable(ABC):
    @abstractmethod
    def draw(self, surface, offset_x=0):
        pass


class Collidable(ABC):
    @abstractmethod
    def get_rect(self):
        pass

    @abstractmethod
    def get_mask(self):
        pass


class GameObject(Drawable, Collidable):
    def __init__(self, x, y, width, height, name=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name
        self.mask = None

    def draw(self, surface, offset_x=0, offset_y=0):
        surface.blit(self.image, (self.rect.x - offset_x, self.rect.y-offset_y))

    def get_rect(self):
        return self.rect

    def get_mask(self):
        return self.mask


class Block(GameObject):
    def __init__(self, x, y, size, image=None):
        super().__init__(x, y, size, size, 'Block')
        if image:
            self.image.blit(image, (0, 0))
        else:
            pygame.draw.rect(self.image, (120, 80, 40), (0, 0, size, size))
        self.mask = pygame.mask.from_surface(self.image)
