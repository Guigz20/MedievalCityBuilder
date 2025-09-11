import pygame as pg
from Scripts.Map.Buildings.building import Building

class Tent(Building):
    def __init__(self, pos: list):
        super().__init__("Tent", pg.image.load("../Assets/Map/Buildings/Habitats/Tent.png").convert_alpha(), pos)

        self.image = pg.transform.scale(self.image, (self.image.get_width()*2, self.image.get_height()*2))
