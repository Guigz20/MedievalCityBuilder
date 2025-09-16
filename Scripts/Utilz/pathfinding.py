

class Pathfinder:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.grid = [[]]


class Node:
    def __init__(self, position: tuple, is_start: bool, is_end: bool):
        self.pos = position
        self.is_start = is_start
        self.is_end = is_end
        self.Fcost = 0
        self.Gcost = 0
        self.Hcost = 0

    def get_cost(self, start_pos, end_pos):
        if not self.is_start and not self.is_end:
            self.Gcost = abs(self.pos[0] - start_pos[0]) + abs(self.pos[1] - start_pos[1])
            self.Hcost = abs(self.pos[0] - end_pos[0]) + abs(self.pos[1] - end_pos[1])
            self.Fcost = self.Gcost + self.Hcost
