import pygame as pg

class Building:
    def __init__(self, name: str, image: pg.Surface, pos: list):
        self.name = name
        self.image = image
        self.pos = pos

    def draw(self, screen: pg.Surface, scale:float, offset: list):
        scaled_image = pg.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        screen.blit(scaled_image, (self.pos[0]+offset[0], self.pos[1]+offset[1]))