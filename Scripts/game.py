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

            self.map.draw()
            self.map.move(dt)

            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        self.map.should_move = True
                        self.map.direction = "up"
                    elif event.key == pg.K_s:
                        self.map.should_move = True
                        self.map.direction = "down"
                    elif event.key == pg.K_a:
                        self.map.should_move = True
                        self.map.direction = "left"
                    elif event.key == pg.K_d:
                        self.map.should_move = True
                        self.map.direction = "right"
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_w or event.key == pg.K_s or event.key == pg.K_a or event.key == pg.K_d:
                        self.map.should_move = False

                elif event.type == pg.QUIT:
                    self.running = False
                    pg.quit()

if __name__ == '__main__':
    game = Game()
    game.loop()


