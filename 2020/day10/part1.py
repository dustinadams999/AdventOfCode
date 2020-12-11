import sys

lines = [int(f.replace('\n', '')) for f in open(sys.argv[1], 'r').readlines()]
lines.sort()

one_jolt = 0
three_jolt = 1
for i in range(0,len(lines)-1):
    if lines[i+1] - lines[i] == 1:
        one_jolt += 1
    elif lines[i+1] - lines[i] == 3:
        three_jolt += 1

# edge case
if lines[0] == 1:
    one_jolt += 1
elif lines[0] == 3:
    one_jolt += 1


print('one jolt: {}, three jolt: {}, product: {}'.format(one_jolt, three_jolt,one_jolt*three_jolt))