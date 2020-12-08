"""
usage: $ python part1.py <input-file>
"""
import numpy as np
import sys

f = open(sys.argv[1],'r')

lines = [a.replace('\n', '') for a in f.readlines()]
visited = np.zeros(len(lines), dtype=bool)

accumulator = 0

i = 0

while i < len(lines):
    if visited[i]:
        print('INFINITE LOOP! acc: {}'.format(accumulator))
        break
    else:
        visited[i] = True
    op = lines[i].split()[0]
    arg = int(lines[i].split()[1])
    if op == 'nop':
        i += 1
        continue
    elif op == 'acc':
        accumulator += arg
        i += 1
    elif op == 'jmp':
        i += arg
        continue
    else:
        '***OPERATION ERROR***'
