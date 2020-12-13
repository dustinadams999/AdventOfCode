"""
usage: $ print part2.py <input-file>
"""
import math
import sys

headings = {
    'N': (lambda way, amount: ((way[0]+amount, way[1]))), # move lat and lon by val
    'E': (lambda way, amount: ((way[0], way[1]+amount))),
    'S': (lambda way, amount: ((way[0]-amount, way[1]))),
    'W': (lambda way, amount: ((way[0], way[1]-amount)))
}
# with forward, we need to subtract an offset of 90 degrees since we treat North as 0 degrees
# but sine and cosine treat East as zero degrees, which we treat as 90 degrees.
forward = {
    'F': (lambda lat, lon, way, amount: ((lat + (way[0]*amount), lon + (way[1]*amount))))
}

rotations = {
    'R': {
        90: (lambda way: ((-1*way[1], way[0]))),
        180: (lambda way: ((-1*way[0], -1*way[1]))),
        270: (lambda way: ((way[1], -1*way[0])))
    },
    'L': {
        90: (lambda way: ((way[1], -1*way[0]))),
        180: (lambda way: ((-1*way[0], -1*way[1]))),
        270: (lambda way: ((-1*way[1], way[0])))
    }
}

lines = [f.replace('\n', '') for f in open(sys.argv[1], 'r').readlines()]

# the waypoint starts at 1 unit north 10 units east, stored as (lat, lon)
way = (1, 10) 

lat = 0 # goes north and south
lon = 0 # goes east and west

coord = (0,0) # lat, lon

for line in lines:
    
    direction = line[0]
    amount = int(line[1:])
    if direction in headings.keys():
        way = headings[direction](way, amount)
    elif direction in rotations.keys():
        way = rotations[direction][amount](way)

    elif direction in forward.keys():
        coord = forward[direction](coord[0], coord[1], way, amount)
    else:
        print('READ ERROR')

print('final way: {}'.format(way))
print('Manhattan Distance: {}'.format(abs(coord[0])+abs(coord[1])))
