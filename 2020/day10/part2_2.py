"""
usage: $ python part2_2.py <input-file>

This script was derived from a post from reddit.com/r/adventofcode explaining
how a combinatorial solution can be found. 
"""
import sys

lines = [int(f.replace('\n', '')) for f in open(sys.argv[1]).readlines()]
lines.sort()
lines.insert(0,0)
lines.append(lines[-1]+3)
print(lines)

deltas = []

two_times=0 # base 2
three_times=0 # base 4
four_times=0 # base 7

for i in range(0,len(lines)-1):
    deltas.append(lines[i+1] - lines[i])

i=0
contig = 1
print(deltas)
while i < (len(deltas)-1):
    contig = 1
    while (i < (len(deltas)-1)) and (deltas[i] == 1 and deltas[i+1]==deltas[i]):
        contig += 1
        i += 1
    if contig == 2:
        two_times += 1
    elif contig == 3:
        three_times += 1
    elif contig == 4:
        four_times += 1
    i += 1
print('two_times: {}, three_times: {}, four_times: {}'.format(two_times,three_times,four_times))
print(pow(2,two_times)*pow(4,three_times)*pow(7,four_times))

#print(deltas)





