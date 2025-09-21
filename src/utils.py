### FILE: src/utils.py
"""
Utility functions: asset loading, simple helpers.
Keep this module small and focused.
"""
import os
from os import listdir
from os.path import isfile, join
import pygame
from config import ASSETS_DIR, TERRAIN_DIR


def safe_load_image(path, colorkey_alpha=True):
    """Load image and convert_alpha; return a Surface or a placeholder Surface.
    This prevents the whole game from crashing if an asset is missing.
    """
    try:
        image = pygame.image.load(path)
        return image.convert_alpha()
    except Exception as e:
        print(f"[WARN] Failed to load image {path}: {e}")
        # return a visible placeholder surface
        surf = pygame.Surface((32, 32))
        surf.fill((0, 0, 255))
        return surf


def list_asset_files(*parts):
    p = join(ASSETS_DIR, *parts)
    if not os.path.exists(p):
        return []
    return [f for f in listdir(p) if isfile(join(p, f))]


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join(ASSETS_DIR, dir1, dir2)
    files = list_asset_files(dir1, dir2)

    all_sprites = {}

    for image in files:
        sprite_sheet = safe_load_image(join(path, image))
        sprites = []
        for i in range(max(1, sprite_sheet.get_width() // width)):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        key = image.replace('.png', '')
        if direction:
            all_sprites[key + '_right'] = sprites
            all_sprites[key + '_left'] = flip(sprites)
        else:
            all_sprites[key] = sprites

    return all_sprites

# all sprite in terrain, so final, need maths later for position
def load_block(size):
    path = join(ASSETS_DIR, TERRAIN_DIR, 'Terrain.png')
    image = safe_load_image(path)
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    # default rect; replace with config or read atlas data later
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)
