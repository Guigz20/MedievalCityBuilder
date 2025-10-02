from idlelib.colorizer import prog_group_name_to_tag

import pygame as pg
from math import *

import pygame.display


class Pathfinder:
    def __init__(self, start_point, end_point, rects, tile_size_scaled: int):
        self.start_point_global = start_point
        self.end_point_global = end_point

        self.tile_size_scaled = tile_size_scaled

        self.selected = []
        self.grid = []

        self.start_tile = Node(start_point, is_start=True)
        self.end_tile = Node(end_point, is_end=True)

        self.rects = rects


        self.end_tile_found = False
        self.first_step = True

        self.Search()

    def NextStep(self):
        if self.first_step:
            self.first_step = False
            self.selected.append(self.start_tile)

        len_selected = len(self.selected)

        for tile in self.selected:
            self.selected.remove(tile)
            len_selected -= 1

            lowest_Fcost_tile = None
            lowest_Fcost = 10000

            for neighbor in self.get_neighbors(tile.pos):
                neighbor_Fcost = neighbor.get_cost(self.end_point_global)

                if lowest_Fcost_tile is not None:
                    print("Lowest: ", lowest_Fcost_tile.get_cost(self.end_point_global), " | ", lowest_Fcost_tile.pos)
                print("Actual: ", neighbor_Fcost, " | ", neighbor.pos)
                print("------------------------------")

                if lowest_Fcost_tile is None:
                    print("Fcost: None")
                    print("------------------------------")
                    lowest_Fcost_tile = neighbor

                elif lowest_Fcost > neighbor_Fcost:
                    print("Fcost: lower")
                    print("------------------------------")
                    lowest_Fcost_tile = neighbor
                    lowest_Fcost = neighbor_Fcost

                elif lowest_Fcost == neighbor_Fcost:
                    if lowest_Fcost_tile.Gcost > neighbor.Gcost:
                        print("Gcost: lower")
                        print("------------------------------")
                        lowest_Fcost_tile = neighbor

                    elif lowest_Fcost_tile.Gcost == neighbor.Gcost:
                        print("Fcost and Gcost: same")
                        print("------------------------------")
                        self.selected.append(neighbor)



                if neighbor.is_end:
                    self.end_tile_found = True
                    print("End tile found")
                    return

            if len_selected == 0:
                break

            self.selected.append(lowest_Fcost_tile)
            print("*********************")
            print(len(self.selected))
            print("*********************")

    def Search(self):
        self.NextStep()
        self.NextStep()
        print("Next step!")

    def blit(self, offset):
        for tile in self.selected:
            print(tile.pos)
            print(self.tile_size_scaled)
            pos = (tile.pos[0]*self.tile_size_scaled+offset[0], tile.pos[1]*self.tile_size_scaled+offset[1])
            pygame.draw.rect(pygame.display.get_surface(), (0, 255, 0), pg.rect.Rect(pos, (self.tile_size_scaled, self.tile_size_scaled)))

    def get_neighbors(self, tile_pos):
        nodes = []

        nodes.append(Node((tile_pos[0] + 1, tile_pos[1])))
        nodes.append(Node((tile_pos[0] - 1, tile_pos[1])))
        nodes.append(Node((tile_pos[0], tile_pos[1] + 1)))
        nodes.append(Node((tile_pos[0], tile_pos[1] - 1)))

        return nodes





class Node:
    def __init__(self, position: tuple, is_start: bool = False, is_end: bool = False, is_solid: bool = False):
        self.pos = position

        self.is_start = is_start
        self.is_end = is_end
        self.is_solid = is_solid

        self.Fcost = 0
        self.Gcost = 0
        self.Hcost = 0
        self.parent = None


    def get_cost(self, end_pos):
        if not self.is_start and not self.is_end:
            self.Gcost = abs(self.pos[0]) + abs(self.pos[1])
            self.Hcost = abs(self.pos[0] - end_pos[0]) + abs(self.pos[1] - end_pos[1])
            self.Fcost = self.Gcost + self.Hcost

            print(f"Fcost: {self.Fcost}, Gcost: {self.Gcost}, Hcost: {self.Hcost}")

        return self.Fcost

    def blit(self, true_pos, tile_size):
        pygame.draw.rect(pygame.display.get_surface(), (0, 255, 0), (self.pos[0]*tile_size + true_pos[0], self.pos[1]*tile_size + true_pos[1], tile_size, tile_size))
