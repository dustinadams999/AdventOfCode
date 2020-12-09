"""
usage: $ python part1.py <input-file>
"""
import sys

f = open(sys.argv[1], 'r')
PREAMBLE_LEN=int(sys.argv[2])
lines = [int(a.replace('\n','')) for a in f.readlines()]
no_sum = -1

for i in range(PREAMBLE_LEN, len(lines)):
    # check if lines[i] is a sum of numbers in the preceding preamble
    found_match = False
    for j in range(i - PREAMBLE_LEN, i):
        for k in range(i - PREAMBLE_LEN, i):
            if (j != k) and (lines[j] + lines[k] == lines[i]):
                found_match = True
    if not found_match:
        print("{} does not have a valid sum".format(lines[i]))
        no_sum = lines[i]
        break
