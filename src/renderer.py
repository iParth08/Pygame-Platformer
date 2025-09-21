
### FILE: src/renderer.py
"""
Renderer is responsible only for drawing and camera offset calculations.
This allows swapping the rendering backend if needed.
"""
import pygame
from config import WIDTH, HEIGHT, SCROLL_AREA_WIDTH, SCROLL_AREA_HEIGHT


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.offset_x = 0
        self.offset_y = 0

    def update_camera(self, player):
        # simple side-scrolling logic
        if (player.rect.right - self.offset_x > WIDTH - SCROLL_AREA_WIDTH and player.x_vel > 0) or (player.rect.left - self.offset_x <= SCROLL_AREA_WIDTH and player.x_vel < 0):
            self.offset_x += player.x_vel
        
        # simple vertical-scrolling logic
        if (player.rect.bottom - self.offset_y > HEIGHT - SCROLL_AREA_HEIGHT and player.y_vel > 0) or (player.rect.top - self.offset_y <= SCROLL_AREA_HEIGHT and player.y_vel < 0):
            self.offset_y += player.y_vel

    def clear(self):
        self.screen.fill((255, 255, 255))

    def draw_background(self, tiles, bg_image):
        for tile in tiles:
            self.screen.blit(bg_image, tile)

    def draw_objects(self, objects):
        for obj in objects:
            obj.draw(self.screen, self.offset_x, self.offset_y)

    def draw_player(self, player):
        player.draw(self.screen, self.offset_x, self.offset_y)

    def present(self):
        pygame.display.update()
