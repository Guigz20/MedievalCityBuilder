import pygame
import pygame as pg
from pygame.examples.grid import TILE_SIZE

from Scripts.Utilz.constants import *
import random

class Map:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.tile_size = 36

        self.map = {}
        self.width, self.height = 0, 0
        self.offset = [0, 0]
        self.blit_offset = [-self.tile_size*INITIAL_SCALE_FACTOR/2, -self.tile_size*INITIAL_SCALE_FACTOR/2]

        self.in_screen_tiles = {}

        self.should_move = False
        self.direction = ""
        self.speed = 120

        self.grass = pg.image.load('../Assets/Map/Images/Grass01.png')
        self.grass_list = [[]]

    def initiate_surface(self, scale_factor):

        for x in range(SCREEN_WIDTH//TILE_SIZE*scale_factor):
            for y in range(SCREEN_HEIGHT//TILE_SIZE*scale_factor):
                scaled_grass = pg.transform.scale(self.grass, (TILE_SIZE*scale_factor, TILE_SIZE*scale_factor))
                rotated_grass = pg.transform.flip(scaled_grass, True, False)
                self.grass_list[x].append(pg.transform.scale(rotated_grass, (TILE_SIZE*scale_factor, TILE_SIZE*scale_factor)))


    def draw(self,scale):
        pygame.draw.circle(self.screen, (255, 0, 0), self.offset, 10)
        pygame.draw.circle(self.screen, (0, 255, 0), self.blit_offset, 10)
        self.scaled_grass = pg.transform.scale(self.grass, (self.tile_size*scale, self.tile_size*scale))
        for x in range(SCREEN_WIDTH//self.tile_size*scale + self.tile_size*scale):
            for y in range(SCREEN_HEIGHT//self.tile_size*scale + self.tile_size*scale):
                x_blit = self.blit_offset[0]+x*self.tile_size*scale-self.tile_size*scale
                y_blit = self.blit_offset[1]+y*self.tile_size*scale-self.tile_size*scale
                self.screen.blit(self.scaled_grass, (x_blit, y_blit))


    def move(self, dt: float, scale: float):

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

        if self.blit_offset[0] < 0:
            self.blit_offset[0] = self.tile_size*scale
        elif self.blit_offset[1] < 0:
            self.blit_offset[1] = self.tile_size*scale
        elif self.blit_offset[0] > self.tile_size*scale:
            self.blit_offset[0] = 0
        elif self.blit_offset[1] > self.tile_size*scale:
            self.blit_offset[1] = 0