"""
usage: $ python part1.py <input-file>
"""
import sys

f = open(sys.argv[1],'r')

lines = [line.replace('\n', '') for line in f.readlines()]

totals = []
group = set()
j = 0
for line in lines:

    if line == '':
        totals.append(len(list(group)))
        group = set()
    elif j == len(lines)-1: # special case for last member
        for i in line:
            group.add(i)
        totals.append(len(list(group)))
    else:
        for i in line:
            group.add(i)

    j += 1

f.close()

print('sum: {}'.format(sum(totals)))