import numpy as np
import sys
from IPython import embed as shell


vals = {
    "first": {
        "U": "|f",
        "D": "|f",
        "L": "-f",
        "R": "-f",
        "T": "+f"
    },
    "second": {
        "U": "|s",
        "D": "|s",
        "L": "-s",
        "R": "-s",
        "T": "+s"
    }
}

def main(dimension):
    dimension = int(dimension)
    x = y = x0 = y0 = int(dimension/2)

    intersections = []
    wires = build_board(dimension)
    # find the intersections
    for i in range(0, dimension):
        for j in range(0, dimension):
            if wires[i][j] == 'X':
                cords = (i,j)
                intersections.append(cords)            
        # print('checking: x:{}, y:{}'.format(i,j))

    print('intersections: {}'.format(intersections))
    print('now calculating shortest path')

    # calculate distance each wire has to travel to the intersection
    #for inter in intersections:
    #wires = np.zeros((dimension,dimension), dtype='<U4')
    #wires[x][y] = 'o'
    f = open(sys.argv[1],'r')


    path = {'wire1': [(x0,y0)], 'wire2': [(x0,y0)]}
    wi = 'wire1'
    for line in f.readlines():
        x = y = x0
        wire = line.replace('\n', '').split(',')
        for w in wire:
            direction = w[0]
            amount = int(w[1:])
            if direction == 'U':
                for i in range(amount):
                    y -= 1
                    coord = (x,y)
                    if (x,y) in path[wi]: # delete all coords previous till x,y
                        index = path[wi].index(coord)
                        path[wi] = path[wi][:index+1]
                    else:
                        path[wi].append(coord)
            elif direction == 'D':
                for i in range(amount):
                    y += 1
                    coord = (x,y)
                    if (x,y) in path[wi]:
                        index = path[wi].index(coord)
                        path[wi] = path[wi][:index+1]
                    else:
                        path[wi].append(coord)
            elif direction == 'L':
                for i in range(amount):
                    x -= 1
                    coord = (x,y)
                    if (x,y) in path[wi]:
                        index = path[wi].index(coord)
                        path[wi] = path[wi][:index+1]
                    else:
                        path[wi].append(coord)
            elif direction == 'R':
                for i in range(amount):
                    x += 1
                    coord = (x,y)
                    if (x,y) in path[wi]:
                        index = path[wi].index(coord)
                        path[wi] = path[wi][:index+1]
                    else:
                        path[wi].append(coord)
        wi = 'wire2'

    min_path = dimension**2
    for inter in intersections:
        # calculate distance from origin to inter for both wires
        path_sum = 0
        for p in path:
            for w in path[p]:
                if w == inter:
                    break
                path_sum += 1
        if path_sum < min_path:
            min_path = path_sum

    print('minimum path: {}'.format(min_path))
            

    # find the closest intersection
    #lowest = intersections[0]

    #for inter in intersections:
    #    print('inter: ({},{}), distance: {}'.format(inter[0],inter[1], abs(inter[0] - x0) + abs(inter[1] - y0)))
    #    if (abs(inter[0] - x0) + abs(inter[1] - y0) <
    #        abs(lowest[0] - x0) + abs(lowest[1] - y0)):
    #        lowest = inter


    #start = (x0,y0)
    #print('start: {}'.format(start))
    #print('lowest intersection: {}'.format(lowest))
    #print('lowest distance: {}'.format(abs(lowest[0] - x0) + abs(lowest[1] - y0)))

def build_board(dimension):
    x = y = x0 = y0 = int(dimension/2)

    wires = np.zeros((dimension,dimension), dtype='<U4')
    wires[x][y] = 'o'
    f = open(sys.argv[1],'r')


    # build the breadboard
    val = 'first'
    for line in f.readlines():
        x = y = x0
        wire = line.replace('\n', '').split(',')
        for w in wire:
            direction = w[0]
            amount = int(w[1:])
            if direction == 'U':
                for i in range(amount):
                    y -= 1
                    if i == amount - 1:
                        wires[x][y] = vals[val]['T']
                    elif wires[x][y] == '':
                        wires[x][y] = vals[val]['U']
                    else:
                        if val == 'second' and 'f' in wires[x][y]:
                            wires[x][y] = 'X'
                        else:
                            wires[x][y] = vals[val]['U']
            elif direction == 'D':
                for i in range(amount):
                    y += 1
                    if i == amount - 1:
                        wires[x][y] = vals[val]['T']
                    elif wires[x][y] == '':
                        wires[x][y] = vals[val]['D']
                    else:
                        if val == 'second' and 'f' in wires[x][y]:
                            wires[x][y] = 'X'
                        else:
                            wires[x][y] = vals[val]['D']
            elif direction == 'L':
                for i in range(amount):
                    x -= 1
                    if i == amount - 1:
                        wires[x][y] = vals[val]['T']
                    elif wires[x][y] == '':
                        wires[x][y] = vals[val]['L']
                    else:
                        if val == 'second' and 'f' in wires[x][y]:
                            wires[x][y] = 'X'
                        else:
                            wires[x][y] = vals[val]['L']
            elif direction == 'R':
                for i in range(amount):
                    x += 1
                    if i == amount - 1:
                        wires[x][y] = vals[val]['T']
                    elif wires[x][y] == '':
                        wires[x][y] = vals[val]['R']
                    else:
                        if val == 'second' and 'f' in wires[x][y]:
                            wires[x][y] = 'X'
                        else:
                            wires[x][y] = vals[val]['R']
        val = 'second'

    return wires

if __name__ == "__main__":
    dimension = sys.argv[2]
    main(dimension)
