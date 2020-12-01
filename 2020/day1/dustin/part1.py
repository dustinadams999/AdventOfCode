import sys

f = open(sys.argv[1], 'r')
items = [int(i) for i in f.readlines()]

for i in items:
    for j in items:
        if i+j == 2020 and i!=j:
            print("product: {}".format(i*j))
