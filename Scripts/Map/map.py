import pygame
import pygame as pg
from pygame.examples.grid import TILE_SIZE

from Scripts.Utilz.constants import *
import random

class Map:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.tile_size = (36, 36)

        self.map = {}
        self.width, self.height = 0, 0
        self.offset = [0, 0]
        self.blit_offset = [-self.tile_size[0]*INITIAL_SCALE_FACTOR, -self.tile_size[1]*INITIAL_SCALE_FACTOR]

        self.initialize()

        self.in_screen_tiles = {}
        self.reset_in_game_tiles(INITIAL_SCALE_FACTOR)

        self.should_move = False
        self.direction = ""
        self.speed = 120

    def initialize(self):
        for x in range(0, 200):
            for y in range(0, 200):
                surface = pg.image.load('../Assets/Map/Images/Grass01.png')
                surface = pg.transform.scale(surface,(self.tile_size[0]*INITIAL_SCALE_FACTOR, self.tile_size[1]*INITIAL_SCALE_FACTOR))
                if random.randint(0, 1) == 0:
                    surface = pg.transform.flip(surface, True, False)
                self.map[(x, y)] = surface
                if y > self.width:
                    self.width = y
            if x > self.height:
                self.height = x
        print(SCREEN_WIDTH//(self.tile_size[0]*INITIAL_SCALE_FACTOR))

    def reset_in_game_tiles(self, scale):
        print("Resetting in-game tiles")
        is_first_tile = True
        for tile in self.map:
            tile_pos_x, tile_pos_y = tile[0]*self.tile_size[0]*scale, tile[1]*self.tile_size[1]*scale
            tile_size = self.tile_size[0]*scale
            if tile_pos_x > self.offset[0]-tile_size and tile_pos_y > self.offset[1]-tile_size:
                if tile_pos_x < self.offset[0]+tile_size+SCREEN_WIDTH and tile_pos_y < self.offset[1]+tile_size+SCREEN_HEIGHT:
                    self.in_screen_tiles[tile] = self.map[tile]
                    if is_first_tile:
                        self.blit_offset = [tile[0]*scale*self.tile_size[0] + self.offset[0], tile[1]*scale*self.tile_size[0] + self.offset[1]]
                        is_first_tile = False

    def draw(self,scale):
        for tile in self.in_screen_tiles:
            self.screen.blit(self.in_screen_tiles[tile], (tile[0]*scale*self.tile_size[0] + self.offset[0], tile[1]*scale*self.tile_size[0] + self.offset[1]))
        if abs(self.blit_offset[0]) >= self.tile_size[0]*scale or abs(self.blit_offset[1]) >= self.tile_size[0]*scale:
            self.reset_in_game_tiles(scale)
            print(self.blit_offset)

    def move(self, dt: int):

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.offset[1] += self.speed * dt
            self.blit_offset[1] += self.speed * dt
        elif keys[pg.K_s]:
            self.offset[1] -= self.speed * dt
            self.blit_offset[1] -= self.speed * dt
        elif keys[pg.K_a]:
            self.offset[0] += self.speed * dt
            self.blit_offset[0] += self.speed * dt
        elif keys[pg.K_d]:
            self.offset[0] -= self.speed * dt
            self.blit_offset[0] -= self.speed * dt