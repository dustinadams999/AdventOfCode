from IPython import embed as shell
import numpy as np
import sys

f = open(sys.argv[1],'r')

lines = [a.replace('\n', '') for a in f.readlines()]

accumulator = 0

line_numbers = [lines.index(a) for a in lines if a.split()[0]=='nop']
line_numbers += [lines.index(a) for a in lines if a.split()[0]=='jmp']

infinite_loop = False
for line_number in line_numbers:
    accumulator = 0
    visited = np.zeros(len(lines), dtype=bool)
    infinite_loop = False
    nop = True
    if 'nop' in lines[line_number]: # replace nop with jmp
        lines[line_number] = 'jmp' + lines[line_number][3:]
    elif 'jmp' in lines[line_number]:
        nop = False
        lines[line_number] = 'nop' + lines[line_number][3:]
    else:
        '***LINE NUMBER ERROR***'
        exit(1)

    i = 0

    while i < len(lines):
        if visited[i]:
            infinite_loop = True
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
            exit(1)

    if i == len(lines):
        shell()
        print('PROGRAM COMPLETION SUCCESS! acc: {}'.format(accumulator))

    elif infinite_loop: # change it back to nop's original value
        if nop:
            lines[line_number] = 'nop' + lines[line_number][3:]
        else:
            lines[line_number] = 'jmp' + lines[line_number][3:]
    else:
        print('***NO COMPLETION OR INFINITE LOOP ERROR***')
