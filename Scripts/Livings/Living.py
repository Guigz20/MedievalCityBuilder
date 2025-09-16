import pygame as pg

from Scripts.Utilz.constants import *


class Living(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.pos = [300, 300]
        self.size = (20, 30)
        self.rect = pg.rect.Rect(self.pos, (self.size[0]*INITIAL_SCALE_FACTOR, self.size[1]*INITIAL_SCALE_FACTOR))

        self.screen = pg.display.get_surface()

    def draw(self, scale):
        self.rect = pg.rect.Rect(self.pos, (self.size[0]*scale, self.size[1]*scale))
        pg.draw.rect(self.screen, (255, 187, 0), self.rect)
