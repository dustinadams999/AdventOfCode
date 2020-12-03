"""
usage: $ python part2.py <input-file>
"""
import numpy as np
import sys

f = open(sys.argv[1], 'r')

grid = np.array([i.replace("\n", "") for i in f.readlines()])

slopes = ((1,1),(3,1),(5,1),(7,1),(1,2))

product = 1
for slope in slopes:
    collisions = 0
    dx=slope[0]
    dy=slope[1]
    x=0
    y=0

    while y < len(grid):
        if grid[y][x] == "#":
            collisions += 1

        x += dx
        x %= len(grid[y])
        y += dy

    product *= collisions

print(product)

