"""
main.py
im pretty sure logic goes here but what do i know
"""

import cells
import screen

screen.x = 40
screen.y = 30
ticknums = 10

icells = [
    [0, cells.dirs['right'], 0] # cell type, direction, id in list
]

tcells = []

grid = [[2,3]]


for i, x in enumerate(icells):
    if x[0] == 0:
        tcells += [[cells.mover(grid[ x[2] ], x[1]), i]]

for _ in range(ticknums):
    for i in tcells:
        i[0].tick(grid)
    for i in tcells:
        screen.clrscn()
        screen.scnmem += [i[0].scrget()]
        screen.updscn()
        screen.getkey()