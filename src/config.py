### FILE: src/config.py
"""
Configuration constants and feature flags.
Single source of truth for tunable values.
"""


WIDTH = 1000
HEIGHT = 650
FPS = 60


# Player defaults
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_START_X = 100
PLAYER_START_Y = 100
PLAYER_VEL = 5
PLAYER_GRAVITY = 1


# Camera / scrolling
SCROLL_AREA_WIDTH = 200
SCROLL_AREA_HEIGHT = 150


# Block / tile settings
TILE_SIZE = 96


# Feature toggles
ENABLE_DEBUG = True
ENABLE_SOUNDS = False # Placeholder: set True after adding assets


# Paths
ASSETS_DIR = "../assets"
BACKGROUND_DIR = "Background"
TERRAIN_DIR = "Terrain"
CHAR_DIR = "MainCharacters"
TRAPS_DIR = "Traps"
MAP_DIR = "../maps/"



# Gameplay
MAX_DOUBLE_JUMP = 2