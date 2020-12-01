import sys

f = open(sys.argv[1], 'r')
items = [int(i) for i in f.readlines()]

for i in items:
    for j in items:
        for k in items:
            if i+j+k == 2020 and i!=j!=k:
                print("product: {}".format(i*j*k))
