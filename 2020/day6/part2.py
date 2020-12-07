"""
usage: $ python part2.py <input-file>
"""
import sys

f = open(sys.argv[1],'r')

lines = [line.replace('\n', '') for line in f.readlines()]

totals = []
group = set()
j = 0
beginning = True
for line in lines:

    if line == '':
        totals.append(len(list(group)))
        group = set()
        beginning = True
    elif j == len(lines)-1: # special case for last member
        if beginning: # first member of the group
            for i in line:
                group.add(i)
        else:
            answers = [i for i in line]
            group = group.intersection(set(answers))

        totals.append(len(list(group)))
    else:
        if beginning: # first member of the group
            for i in line:
                group.add(i)
            beginning = False
        else:
            answers = [i for i in line]
            group = group.intersection(set(answers))

    j += 1

f.close()

print('sum: {}'.format(sum(totals)))