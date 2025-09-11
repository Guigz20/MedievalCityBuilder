import math

import pygame
import pygame as pg

from Scripts.Map.Buildings.Habitats.Tent import Tent
from Scripts.Utilz.constants import *
from Scripts.Map.Buildings.Habitats.Tent import Tent

import random

class Map:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.tile_size = 36

        self.buildings = []
        self.buildings.append(Tent([100, 100]))

        self.offset = [0, 0]
        self.blit_offset = [-self.tile_size*INITIAL_SCALE_FACTOR/2, -self.tile_size*INITIAL_SCALE_FACTOR/2]

        self.in_screen_tiles = {}

        self.should_move = False
        self.speed = 200

        self.grass = pg.image.load('../Assets/Map/Images/Grass02.png')

    """ Draws the map to screen """
    def draw(self,scale):

        """Draws the grass background"""
        self.scaled_grass = pg.transform.scale(self.grass, (self.tile_size*scale, self.tile_size*scale))
        for x in range(int(SCREEN_WIDTH//self.tile_size*scale + 2)):
            for y in range(int(SCREEN_HEIGHT//self.tile_size*scale + 2)):
                x_blit = self.blit_offset[0]+x*self.tile_size*scale-self.tile_size*scale
                y_blit = self.blit_offset[1]+y*self.tile_size*scale-self.tile_size*scale
                self.screen.blit(self.scaled_grass, (x_blit, y_blit))

        """Draws all the buildings"""
        for building in self.buildings:
            building.draw(self.screen, scale, self.offset)

    """ Executes when zoom button is pressed, centers the zoom """
    def on_zoom(self, scale_increment: float, scale:float, increasing = bool):

        x = SCREEN_WIDTH * scale_increment
        y = SCREEN_HEIGHT * scale_increment

        if increasing:

            self.offset[0] -= x
            self.offset[1] -= y

            self.move_blit_offset(-x, 0, scale)
            self.move_blit_offset(0, -y, scale)
        else:
            self.offset[0] += x
            self.offset[1] += y

            self.move_blit_offset(x, 0, scale)
            self.move_blit_offset(0, y, scale)

        #print(SCREEN_WIDTH * scale_increment)
        #print(self.offset)
        #print(self.blit_offset)

    """ Move blit_offset without escaping boudaries """
    def move_blit_offset(self, x, y, scale):
        if abs(x) >= self.tile_size*scale:
            self.blit_offset[0] += x/self.tile_size*scale - int(x/self.tile_size*scale)
            print(x/self.tile_size*scale - int(x/self.tile_size*scale))
            print(self.blit_offset)
        else:
            self.blit_offset[0] += x
        if abs(y) >= self.tile_size*scale:
            self.blit_offset[1] += y/self.tile_size*scale - int(y/self.tile_size*scale)
        else:
            self.blit_offset[1] += y

        if self.blit_offset[0] < 0:
            self.blit_offset[0] = self.tile_size*scale
        elif self.blit_offset[1] < 0:
            self.blit_offset[1] = self.tile_size*scale
        elif self.blit_offset[0] > self.tile_size*scale:
            self.blit_offset[0] = 0
        elif self.blit_offset[1] > self.tile_size*scale:
            self.blit_offset[1] = 0

    """ Moves the entire map's offset and blit offset"""
    def move(self, dt: float, scale: float):

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.offset[1] += self.speed * dt
            self.move_blit_offset(0, self.speed*dt, scale)
        elif keys[pg.K_s]:
            self.offset[1] -= self.speed * dt
            self.move_blit_offset(0, -self.speed*dt, scale)
        elif keys[pg.K_a]:
            self.offset[0] += self.speed * dt
            self.move_blit_offset(self.speed * dt, 0, scale)
        elif keys[pg.K_d]:
            self.offset[0] -= self.speed * dt
            self.move_blit_offset(-self.speed*dt, 0, scale)

