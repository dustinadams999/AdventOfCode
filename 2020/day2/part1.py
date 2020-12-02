"""
usage: $ python part2.py <input-file>
"""
import sys

f = open(sys.argv[1])

valid = 0

for line in f.readlines():
    code = line.split()[2]
    low_bound = int(line.split()[0].split('-')[0])
    high_bound = int(line.split()[0].split('-')[1])
    letter = line.split()[1][0]

    count = len([i for i in code if i == letter])

    if low_bound <= count <= high_bound:
        valid += 1

print(valid)
