"""
cells.py

cells goes heres
"""

import enum

class dirs(enum.Enum):
    up=0
    right=1
    down=2
    left=3
    
    def __int__(value):
        return value.value

class cell:
    class mover:
        symbol = "^>v<"
        curpos = [0,0]
        id = -1
        class can:
            rotate = True
            bemoved = [True, True, True, True]
        direction = -1
        def __repr__(self):
            return "<cell Mover id %d [\'%s\'] at position %s, facing %d>" % (self.id, self.scrget()[2], str(self.curpos), self.direction)
        def __init__(self, pos, dir, id):
            self.curpos = pos
            self.direction = int(dir)
            self.id = id
            print(self.curpos, self.direction, self.id)
        def tick(self, grid):
            dir = self.direction
            curpos = self.curpos
            thisgrid = grid
            curpos = grid[self.id]
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
            thisgrid[self.id] = curpos
            return thisgrid
        def scrget(self):
            curpos = self.curpos
            symbol = self.symbol
            direction = self.direction
            return [curpos[0], curpos[1], symbol[direction]]
    class CWrotator:
        class can:
            bemoved = [True, True, True, True]
            rotate = False
        symbol = "R"
        curpos = [0,0]
        id = -1
        def __repr__(self):
            return "<cell CWrotator id %d [\'%s\'] at position %s>" % self
        def __init__(self, pos, dir, id):
            self.curpos = pos
            # self.direction = int(dir) # rotators cant be rotated... so this is uneeded
            self.id = id
            print(self.curpos, self.direction, self.id)