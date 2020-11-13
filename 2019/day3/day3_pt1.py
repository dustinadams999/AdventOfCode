import numpy as np
import sys

board = np.zeros((200,200), dtype='bool')

x = 100
y = 100

wires = []

wires[x][y] = True 

def main():
    f = open(sys.argv[1],'r')
    for line in f.readlines():
        wire = line.split(',')
        for w in wire:
            direction = w[0]
            amount = int(w[1:])
            if direction == 'U':
                for i in range(amount):
                    y += 1
                    wires[x][y] = True
            elif direction == 'D':
                for i in range(amount):
                    y -= 1
                    wires[x][y] = True
            elif direction == 'L':
                for i in range(amount):
                    x -= 1
                    wires[x][y] = True
            elif direction == 'R':
                for i in range(amount):
                    x += 1
                    wires[x][y] = True
        wires.append(wire)

if __name__ == "__main__":
    main()
