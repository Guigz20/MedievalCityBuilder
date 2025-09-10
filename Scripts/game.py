import pygame as pg
import pygame.joystick

from Utilz.constants import *
from Map.map import Map

class Game:
    def __init__(self):
        pg.init()
        pg.joystick.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption('CityBuilder')
        self.clock = pg.time.Clock()

        self.running = True

        self.scale_factor = INITIAL_SCALE_FACTOR
        self.scale_increment = 0.25

        self.map = Map()

        self.joysticks = {}

        #print(pygame.joystick.get_count())

    def loop(self):
        while self.running:
            dt = self.clock.tick(120)/1000
            #print(self.clock.get_fps())
            self.screen.fill((0,0,0))

            self.map.draw(self.scale_factor)
            self.map.move(dt, self.scale_factor)

            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.JOYDEVICEADDED:
                    joystick = pygame.joystick.Joystick(event.device_index)
                    self.joysticks[joystick.get_instance_id()] = joystick
                    print(f"Joystick {joystick.get_instance_id()} added! ")
                elif event.type == pg.JOYBUTTONDOWN:
                    print(event.button)
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        self.scale_factor += self.scale_increment
                        self.map.on_zoom(self.scale_factor, True)
                    elif event.key == pg.K_DOWN:
                        if self.scale_factor > 1:
                            self.scale_factor -= self.scale_increment
                            self.map.on_zoom(self.scale_factor, False)

                elif event.type == pg.QUIT:
                    self.running = False
                    pg.quit()

if __name__ == '__main__':
    game = Game()
    game.loop()


