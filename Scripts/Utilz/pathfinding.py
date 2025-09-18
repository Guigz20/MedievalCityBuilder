import pygame as pg
from math import *

class Pathfinder:
    def __init__(self, start_point, end_point, rects, tile_size_scaled: int):
        self.start_point_global = start_point
        self.end_point_global = end_point
        self.tile_size_scaled = tile_size_scaled

        self.local_end_point = (trunc(self.end_point_global[0]/self.tile_size_scaled),
                                trunc(self.end_point_global[1]/self.tile_size_scaled))

        self.selected = []
        self.grid = []

        self.start_tile = Node(start_point, is_start=True)
        self.end_tile = Node(end_point, is_end=True)

        self.rects = rects


        self.end_tile_found = False
        self.first_step = True

    def NextStep(self):
        if self.first_step:
            self.first_step = False
            self.selected.append(self.start_tile)

        for tile in self.selected:
            self.selected.remove(tile)

            lowest_Fcost_tile = None
            lowest_Fcost = 10000
            for neighbor in self.get_neighbors(tile.pos):
                neighbor_Fcost = neighbor.get_cost(self.local_end_point)
                if lowest_Fcost_tile is None:
                    lowest_Fcost_tile = neighbor
                elif lowest_Fcost > neighbor_Fcost:
                    lowest_Fcost_tile = neighbor
                    lowest_Fcost = neighbor_Fcost
                elif lowest_Fcost == neighbor_Fcost:
                    if lowest_Fcost_tile.Gcost > neighbor.Gcost:
                        lowest_Fcost_tile = neighbor
                    elif lowest_Fcost_tile.Gcost == neighbor.Gcost:
                        self.selected.append(neighbor)
                if neighbor.is_end:
                    self.end_tile_found = True
                    print("End tile found")
                    return
            self.selected.append(lowest_Fcost_tile)

    def Search(self):
        while not self.end_tile_found:
            self.NextStep()


    def get_neighbors(self, tile_pos):
        nodes = []
        local_tile_pos = (self.start_point_global[0]+tile_pos[0]*self.tile_size_scaled,
                          self.start_point_global[1]+tile_pos[1]*self.tile_size_scaled)
        for rect in self.rects:
            if not rect.colliderect(pg.Rect(local_tile_pos[0]+self.tile_size_scaled, local_tile_pos[1],
                                            self.tile_size_scaled, self.tile_size_scaled)):
                nodes.append(Node((tile_pos[0]+1, tile_pos[1])))
            if not rect.colliderect(pg.Rect(local_tile_pos[0]-self.tile_size_scaled, local_tile_pos[1],
                                            self.tile_size_scaled, self.tile_size_scaled)):
                nodes.append(Node((tile_pos[0]-1, tile_pos[1])))
            if not rect.colliderect(pg.Rect(local_tile_pos[0], local_tile_pos[1]+self.tile_size_scaled,
                                            self.tile_size_scaled, self.tile_size_scaled)):
                nodes.append(Node((tile_pos[0], tile_pos[1]+1)))
            if not rect.colliderect(pg.Rect(local_tile_pos[0], local_tile_pos[1]-self.tile_size_scaled,
                                            self.tile_size_scaled, self.tile_size_scaled)):
                nodes.append(Node((tile_pos[0], tile_pos[1]-1)))

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
        return self.Fcost
