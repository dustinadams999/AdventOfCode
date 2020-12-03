"""
usage: $ python part1.py <input-file>
"""
import sys

import numpy as np

f = open(sys.argv[1], 'r')

grid = [i.replace("\n", "") for i in f.readlines()]

grid = np.array(grid)

collisions = 0

dx=3
dy=1
x=0
y=0
while y < len(grid):
    if grid[y][x] == "#":
        collisions += 1
    x += dx
    x %= len(grid[y])
    y += dy

print(collisions)

