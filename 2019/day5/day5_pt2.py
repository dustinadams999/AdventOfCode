import sys
import numpy as np

codes = []
f = open(sys.argv[1], 'r')
codes = np.array(f.read().replace('\n', '').split(','), dtype='int32')

i=0
while i < len(codes):
    opp_code = codes[i]%100
    par_modes = np.array([np.int32(c) for c in str(codes[i]//100)[::-1]], dtype='int32')
    if opp_code == 1:
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
        else:
            r_op = codes[codes[i+2]]
        codes[codes[i+3]] = l_op + r_op
        i += 4
    elif opp_code == 2:
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
        else:
            r_op = codes[codes[i+2]]
        codes[codes[i+3]] = l_op * r_op
        i += 4
    elif opp_code == 3:
        codes_input = np.int32(input())
        codes[codes[i+1]] = np.int32(codes_input)
        i += 2
    elif opp_code == 4:
        if par_modes[0] == 0:
            print(codes[codes[i+1]])
        elif par_modes[0] == 1:
            print(codes[i+1])
        else:
            print('OPP CODE 4 ERROR')
        i += 2
    elif opp_code == 99 or codes[i+1]%100 == 99:
        print('HALT')
        break
