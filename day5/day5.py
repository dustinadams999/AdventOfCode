import sys
import numpy as np

from IPython import embed as shell

f = open(sys.argv[1], 'r')

target = sys.argv[2]
codes = []
#for a in range(0,99):
#    for b in range(0,99):
f = open(sys.argv[1], 'r')
codes = f.read().replace('\n', '').split(',')

codes = np.array(codes, dtype='int32')

#codes[1] = a
#codes[2] = b

i=0
while i < len(codes):
    opp_code = codes[i]%100
    par_modes = np.array([np.int32(c) for c in str(codes[i]//100)[::-1]], dtype='int32')
    if opp_code == 1:
        l_op = codes[codes[i+1]]
        r_op = codes[codes[i+2]]
        if len(par_modes) >= 1:
            if par_modes[0] == 1:
                l_op = codes[i+1]
        if len(par_modes) >= 2:
            if par_modes[1] == 1:
                r_op = codes[i+1]
        codes[codes[i+2]] = l_op + r_op
        #codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
        i += 4
    elif opp_code == 2:
        l_op = codes[codes[i+1]]
        r_op = codes[codes[i+2]]
        if len(par_modes) >= 1:
            if par_modes[0] == 1:
                l_op = codes[i+1]
        if len(par_modes) >= 2:
            if par_modes[1] == 1:
                r_op = codes[i+1]
        codes[codes[i+2]] = l_op * r_op
        #codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
        i += 4
    elif opp_code == 3:
        codes[codes[i+1]] = np.int32(input())
        i += 2
    elif opp_code == 4:
        print(codes[codes[i+1]])
        i += 2
    elif opp_code == 99:
        print('HALT')
        break
                
        #if codes[0] == int(target):
        #   print('answer: {}'.format(100*codes[1]+codes[2]))
        #   exit(0)


