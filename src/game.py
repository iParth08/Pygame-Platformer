### FILE: src/game.py
"""
Main game orchestration (follows SRP):
- initialize systems
- run the main loop: input -> update -> render
"""
import pygame
from config import WIDTH, HEIGHT, FPS, TILE_SIZE, MAP_DIR
from utils import load_block, safe_load_image
from player import Player
from objects import Block
from traps import Fire
from renderer import Renderer
from input_handler import InputHandler
from level_loader import load_level_from_json


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Mr Platformer — Refactored')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        # systems
        self.renderer = Renderer(self.screen)
        self.input_handler = InputHandler()

        # placeholder: background loader
        self.background, self.bg_image = self.get_background('Pink.png')

        # player
        self.player = Player(100, 100)

        # Game stage
        self.level = 0
        self.meta = {}

        # World
        self.blocks = []
        self.traps = []
        self.objects = []

        # load default level (placeholder)
        if self.level == -1:
            self.load_default_world()
        else:
            self.load_level_map()

        # flags
        self.running = True

    def get_background(self, color_name):
        image = safe_load_image('../assets/Background/' + color_name)
    
        # tile coords
        tiles = []
        w, h = image.get_rect().width, image.get_rect().height
        for i in range(WIDTH // w + 1):
            for j in range(HEIGHT // h + 1):
                tiles.append((i * w, j * h))
        return tiles, image
    

    def load_level_map(self):
        path = MAP_DIR + "level_" + str(self.level) + ".json"
        blocks, traps, meta = load_level_from_json(path)

        self.blocks.extend(blocks)
        self.traps.extend(traps)
        self.meta = meta

        self.refresh_objects()


    def load_default_world(self):
            # REFACTOR THIS AND MANAGE THIS
        block_image = load_block(TILE_SIZE)
        # floor
        floor = [Block(i * TILE_SIZE, HEIGHT - TILE_SIZE, TILE_SIZE, block_image) for i in range(-WIDTH // TILE_SIZE, (WIDTH * 2) // TILE_SIZE)]
        self.blocks.extend(floor)

        # sample obstacles
        self.blocks.append(Block(0, HEIGHT - TILE_SIZE * 2, TILE_SIZE, block_image ))
        self.blocks.append(Block(TILE_SIZE, HEIGHT - TILE_SIZE * 4, TILE_SIZE, block_image))

        # fire
        self.traps.append(Fire(int(TILE_SIZE * 1.5 - 16), int(HEIGHT - TILE_SIZE * 4 - 64), 16, 32))

        self.refresh_objects()

    def refresh_objects(self):
        self.objects = [*self.blocks, *self.traps]

    def handle_collisions(self, dy):
        collided = []
        for obj in self.objects:
            if pygame.sprite.collide_mask(self.player, obj):
                if dy > 0:
                    self.player.rect.bottom = obj.rect.top
                    self.player.landed()
                elif dy < 0:
                    self.player.rect.top = obj.rect.bottom
                    self.player.hit_head()
                collided.append(obj)
        return collided

    def preemptive_collide(self, dx):
        # move player temporarily to test collision
        self.player.move(dx, 0)
        self.player.update()
        collided = None
        for obj in self.objects:
            if pygame.sprite.collide_mask(self.player, obj):
                collided = obj
                break
        # move back
        self.player.move(-dx, 0)
        self.player.update()
        return collided

    def handle_movement(self):
        # inputs
        keys = pygame.key.get_pressed()
        gap = 1
        collide_left = self.preemptive_collide(-5 - gap)
        collide_right = self.preemptive_collide(5 + gap)

        self.player.x_vel = 0
        if keys[pygame.K_LEFT] and not collide_left:
            self.player.move_left(5)
        if keys[pygame.K_RIGHT] and not collide_right:
            self.player.move_right(5)

        vertical_collide_objs = self.handle_collisions(self.player.y_vel)
        to_check = [collide_left, collide_right, *vertical_collide_objs]
        for obj in to_check:
            if obj and getattr(obj, 'name', None) == 'Fire':
                self.player.hit()

    def run_single_frame(self):
        self.input_handler.poll()
        if self.input_handler.get_quit():
            self.running = False
            return

        # event driven jump
        if self.input_handler.is_jump_pressed() and self.player.jump_count < 2:
            self.player.jump()

        # update
        self.player.loop(FPS)
        for t in self.traps:
            t.on() if hasattr(t, 'on') else None
            t.loop(FPS)

        self.handle_movement()

        # render
        self.renderer.clear()
        self.renderer.draw_background(self.background, self.bg_image)
        self.renderer.draw_objects(self.objects)
        self.renderer.draw_player(self.player)
        self.renderer.present()

        # camera
        self.renderer.update_camera(self.player)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.run_single_frame()

        pygame.quit()

