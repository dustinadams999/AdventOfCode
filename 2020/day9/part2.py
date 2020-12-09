"""
usage: $ python part2.py <input-file>
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

# now go back through and find the contiguous set of numbers that sum to no_sum
j = 0
while j < len(lines):
    contig_sum = 0
    i = j
    smallest = lines[i]
    largest = lines[i]
    while contig_sum < no_sum:
        contig_sum += lines[i]
        if lines[i] > largest:
            largest = lines[i]

        if lines[i] < smallest:
            smallest = lines[i]
        
        i += 1

    if contig_sum == no_sum:
        print('WE FOUND THE SET. smallest: {}, largest: {}, sum of the two: {}'.format(smallest,largest,smallest+largest))
        break

    j += 1
