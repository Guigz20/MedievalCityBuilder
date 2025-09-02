import pygame
import pygame as pg
from Scripts.Utilz.constants import *
import random

class Map:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.tile_size = (36, 36)

        self.map = {}
        self.width, self.height = 0, 0
        self.offset = [0, 0]

        self.initialize()
        self.surface = self.redraw_surface(INITIAL_SCALE_FACTOR)

        self.should_move = False
        self.direction = ""
        self.speed = 40

    def initialize(self):
        for x in range(0, SCREEN_WIDTH//(self.tile_size[0]*INITIAL_SCALE_FACTOR) + 1):
            for y in range(0, SCREEN_HEIGHT//(self.tile_size[0]*INITIAL_SCALE_FACTOR) + 1):
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

    def redraw_surface(self, scale):
        surface = pg.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        for tile in self.map:
            surface.blit(self.map[tile], (tile[0]*self.tile_size[0]*scale, tile[1]*self.tile_size[0]*scale))
        return surface

    def draw(self):
        self.screen.blit(self.surface, (self.offset[0], self.offset[1]))

    def move(self, dt: int):
        if self.should_move:
            if self.direction == "right":
                self.offset[0] -= self.speed*dt
            elif self.direction == "left":
                self.offset[0] += self.speed*dt
            elif self.direction == "up":
                self.offset[1] += self.speed*dt
            elif self.direction == "down":
                self.offset[1] -= self.speed*dt