import re
import sys

input_range = sys.argv[1]

low = int(input_range.split('-')[0])
high = int(input_range.split('-')[1])

count = 0

for i in range(low,high):
    double = False # double character repititions
    non_de = True # non decreasing
    tmp = str(i)
    prev = chr(0) # something we know it can't be
    # determine if the number is non decreasing
    for t in tmp:
        if ord(prev) > ord(t):
            non_de = False
            break
        prev = t

    groups = [m.group(0) for m in re.finditer(r"(\d)\1*", tmp)]
    for g in groups:
        if len(g) == 2:
            double = True

    if double and non_de: 
        print(i)
        count += 1 

print('total number: {}'.format(count))
