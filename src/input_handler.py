
### FILE: src/input_handler.py
"""
Encapsulate input operations. This decouples player logic from pygame
and helps follow DIP.
"""
import pygame


class InputHandler:
    def __init__(self):
        self._keys = None
        self._events = []

    def poll(self):
        self._events = pygame.event.get()
        self._keys = pygame.key.get_pressed()

    def is_left(self):
        return self._keys[pygame.K_LEFT]

    def is_right(self):
        return self._keys[pygame.K_RIGHT]

    def is_jump_pressed(self):
        # return True only on KEYDOWN events for space
        for e in self._events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                return True
        return False

    def get_quit(self):
        for e in self._events:
            if e.type == pygame.QUIT:
                return True
        return False
