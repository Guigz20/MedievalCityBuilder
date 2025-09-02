import pygame as pg
from Utilz.constants import *
from Map.map import Map

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('CityBuilder')
        self.clock = pg.time.Clock()

        self.running = True
        self.scale_factor = INITIAL_SCALE_FACTOR

        self.map = Map()

    def loop(self):
        while self.running:
            dt = self.clock.tick(120)/1000
            #print(self.clock.get_fps())
            self.screen.fill((0,0,0))

            self.map.draw(self.scale_factor)
            self.map.move(dt)

            pg.display.flip()
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()

if __name__ == '__main__':
    game = Game()
    game.loop()


