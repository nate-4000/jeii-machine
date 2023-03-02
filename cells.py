"""
cells.py

cells goes heres
"""

import enum

class dirtuple(enum.Enum):
    up=0
    right=1
    down=2
    left=3
    
    def __int__(value):
        return value.value

class mover:
    symbol = "^>v<"
    curpos = [0,0]
    class can:
        rotate = True
        bemoved = True
    direction = -1
    def __init__(self, pos: tuple, dir):
        self.curpos[0] = pos[0]
        self.curpos[1] = pos[1]
        self.direction = int(dir)
        print(self.curpos, self.direction)
    def tick(self, grid):
        dir = self.direction
        if dir == 0:
            if not [curpos[0], curpos[1] + 1] in grid:
                curpos[1] += 1
        elif dir == 1:
            if not [curpos[0] + 1, curpos[1]] in grid:
                curpos[0] += 1
        elif dir == 2:
            if not [curpos[0], curpos[1] - 1] in grid:
                curpos[1] -= 1
        elif dir == 3:
            if not [curpos[0] - 1, curpos[1]] in grid:
                curpos[0] -= 1
        else:
            pass
    def scrget():
        return [curpos[0], curpos[1], symbol[direction]]