"""
usage: $ print part1.py <input-file>
"""
import math
import sys

headings = {
    'N': (lambda lat, lon, amount: ((lat+amount, lon))), # move lat and lon by val
    'E': (lambda lat, lon, amount: ((lat, lon+amount))),
    'S': (lambda lat, lon, amount: ((lat-amount, lon))),
    'W': (lambda lat, lon, amount: ((lat, lon-amount))),
}

directions = {
    'R': (lambda heading, amount: (heading+amount)%360),
    'L': (lambda heading, amount: (heading-amount)%360)
}

# with forward, we need to subtract an offset of 90 degrees since we treat North as 0 degrees
# but sine and cosine treat East as zero degrees, which we treat as 90 degrees.
forward = {
    'F': (lambda heading, amount: ((lat + int(math.sin(math.radians((heading*(-1))+90)))*amount, lon + int(math.cos(math.radians((heading*(-1))+90)))*amount)))
}

lines = [f.replace('\n', '') for f in open(sys.argv[1], 'r').readlines()]

heading = 90

lat = 0 # goes north and south
lon = 0 # goes east and west

for line in lines:
    direction = line[0]
    amount = int(line[1:])

    if direction in headings.keys():
        (lat, lon) = headings[direction](lat, lon, amount)
    elif direction in directions.keys():
        heading = directions[direction](heading, amount)
    elif direction in forward.keys():
        (lat, lon) = forward[direction](heading, amount)

print('final lat: {}, lon: {}'.format(lat,lon))
print('Manhattan Distance: {}'.format(abs(lat)+abs(lon)))
