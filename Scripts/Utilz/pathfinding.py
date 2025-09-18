import pygame as pg

class Pathfinder:
    def __init__(self, start_point, end_point, rects, tile_size_scaled: int):
        self.start_point_global = start_point
        self.end_point_global = end_point

        self.selected = []
        self.grid = []

        self.start_tile = Node(start_point, is_start=True)
        self.end_tile = Node(end_point, is_end=True)

        self.rects = rects
        self.tile_size_scaled = tile_size_scaled

    def NextStep(self):
        pass

    def get_neighbors(self, tile_pos):
        nodes = []
        for rect in self.rects:
            pass
            #if not rect.colliderect(pg.Rect(self.start_point_global[0]+self.tile_size_scaled, self.start_point_global[1], self.tile_size_scaled, self.tile_size_scaled)):
                #nodes.append(Node(tile_pos))





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


    def get_cost(self, start_pos, end_pos):
        if not self.is_start and not self.is_end:
            self.Gcost = abs(self.pos[0] - start_pos[0]) + abs(self.pos[1] - start_pos[1])
            self.Hcost = abs(self.pos[0] - end_pos[0]) + abs(self.pos[1] - end_pos[1])
            self.Fcost = self.Gcost + self.Hcost
