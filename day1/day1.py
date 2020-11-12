# fuel req.d = round_down(mass / 3) - 2
import sys
f = open(sys.argv[1],'r')

total = 0
for i in f.readlines():
    print('calculating')
    fuel = int(i)//3 - 2
    while fuel >= 0:
        total += fuel
        fuel = fuel//3 -2

print('second: {}'.format(total))
