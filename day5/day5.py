import sys
import numpy as np

from IPython import embed as shell

#f = open(sys.argv[1], 'r')

#target = sys.argv[2]
codes = []
#for a in range(0,99):
#    for b in range(0,99):
f = open(sys.argv[1], 'r')
codes = np.array(f.read().replace('\n', '').split(','), dtype='int32')

#codes = np.array(codes, dtype='int32')

#codes[1] = a
#codes[2] = b

i=0
while i < len(codes):
    #shell()
    #print(i)
    opp_code = codes[i]%100
    print('opp_code: {}'.format(opp_code))
    par_modes = np.array([np.int32(c) for c in str(codes[i]//100)[::-1]], dtype='int32')
    if opp_code == 1:
        print('{},{},{},{}'.format(codes[i],codes[i+1],codes[i+2],codes[i+3]))
        l_op = codes[i+1]
        r_op = codes[i+2]
        if len(par_modes) >= 1:
            if par_modes[0] == 1:
                l_op = codes[i+1]
            elif par_modes[0] == 0:
                l_op = codes[codes[i+1]]
        if len(par_modes) >= 2:
            if par_modes[1] == 1:
                r_op = codes[i+2]
            elif par_modes[1] == 0:
                r_op = codes[codes[i+2]]
        codes[codes[i+3]] = l_op + r_op
        #codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
        i += 4
    elif opp_code == 2:
        print('{},{},{},{}'.format(codes[i],codes[i+1],codes[i+2],codes[i+3]))
        l_op = codes[i+1]
        r_op = codes[i+2]
        if len(par_modes) >= 1:
            if par_modes[0] == 1:
                l_op = codes[i+1]
            elif par_modes[0] == 0:
                l_op = codes[codes[i+1]]
        if len(par_modes) >= 2:
            if par_modes[1] == 1:
                r_op = codes[i+2]
            elif par_modes[1] == 0:
                r_op = codes[codes[i+2]]
        codes[codes[i+3]] = l_op * r_op
        #codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
        i += 4
    elif opp_code == 3:
        #print('{},{}'.format(codes[i],codes[i+1]))
        codes_input = np.int32(input())
        codes[codes[i+1]] = np.int32(codes_input)
        i += 2
    elif opp_code == 4:
        #print('{},{}'.format(codes[i],codes[i+1]))
        print(codes[codes[i+1]])
        i += 2
    elif opp_code == 99 or codes[i+1]%100 == 99:
        print('HALT')
        break
               
        #if codes[0] == int(target):
        #   print('answer: {}'.format(100*codes[1]+codes[2]))
        #   exit(0)


