import pygame as pg
from Utilz.constants import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('CityBuilder')
        self.clock = pg.time.Clock()

        self.running = True

    def loop(self):
        while self.running:
            dt = self.clock.tick(120)/1000

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()

if __name__ == '__main__':
    game = Game()
    game.loop()


