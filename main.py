"""
main.py
im horrible at this
"""

import cells
import screen

screen.x = 40
screen.y = 30
ticknums = 10

icells = [
    [0, cells.dirs['right'], 0], # cell type, direction, id in list
    [0, cells.dirs['left'], 1]
]

tcells = []

grid = [
    [10,3], # position of cell with this id
    [30,3]
]



for i, x in enumerate(icells):
    if x[0] == 0:
        tcells += [[cells.cell.mover(grid[ x[2] ], x[1], i)]]
    print(tcells)

for _ in range(ticknums):
    for i in tcells:
        grid = i[0].tick(grid)
    screen.clrscn()
    for i in tcells:
        screen.pushp(*i[0].scrget(), r=False)
        print("screen.scnmem", screen.scnmem)
    screen.updscn()
    #print("screen.scnmem", screen.scnmem)
    print("grid", grid)
    screen.getkey()
