import sys
import numpy as np
from IPython import embed as shell
from itertools import permutations


def main(perms):
    amp_output_signal = [0,0,0,0,0]
    total = []
    # this is what we're using as the index to go through each amp
    for perm in perms:
        amp_index = 0 # will get used for the output signal
        for amp in perm:
            amp = int(amp)
            codes = []
            f = open(sys.argv[1], 'r')
            codes = np.array(f.read().replace('\n', '').split(','), dtype='int32')
            f.close()

            first = True
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
                        else:
                            print('OPP CODE 1 ERROR')
                            exit(1)
                    if len(par_modes) >= 2:
                        if par_modes[1] == 1:
                            r_op = codes[i+2]
                        elif par_modes[1] == 0:
                            r_op = codes[codes[i+2]]
                        else:
                            print('OPP CODE 1 ERROR')
                            exit(1)
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
                        else:
                            print('OPP CODE 2 ERROR')
                            exit(1)
                    if len(par_modes) >= 2:
                        if par_modes[1] == 1:
                            r_op = codes[i+2]
                        elif par_modes[1] == 0:
                            r_op = codes[codes[i+2]]
                        else:
                            print('OPP CODE 2 ERROR')
                            exit(1)
                    else:
                        r_op = codes[codes[i+2]]
                    codes[codes[i+3]] = l_op * r_op
                    i += 4
                elif opp_code == 3:
                    # the phase setting
                    codes_input = amp
                    if not first:    
                        codes_input = 0
                        if amp_index > 0:
                            codes_input = amp_output_signal[amp_index - 1]
                        
                    codes[codes[i+1]] = np.int32(codes_input)
                    i += 2
                    first = False
                elif opp_code == 4:
                    if par_modes[0] == 0:
                        amp_output_signal[amp_index] = codes[codes[i+1]]
                    elif par_modes[0] == 1:
                        amp_output_signal[amp_index] = codes[codes[i+1]]
                    else:
                        print('OPP CODE 4 ERROR')
                        exit(1)
                    i += 2
                elif opp_code == 5:
                    l_op = codes[i+1]
                    r_op = codes[i+2]
                    if len(par_modes) >= 1:
                        if par_modes[0] == 1:
                            l_op = codes[i+1]
                        elif par_modes[0] == 0:
                            l_op = codes[codes[i+1]]
                        else:
                            print('OPP CODE 2 ERROR')
                            exit(1)
                    if len(par_modes) >= 2:
                        if par_modes[1] == 1:
                            r_op = codes[i+2]
                        elif par_modes[1] == 0:
                            r_op = codes[codes[i+2]]
                        else:
                            print('OPP CODE 5 ERROR')
                            exit(1)
                    else:
                        r_op = codes[codes[i+2]]
                    if l_op != 0:
                        i = r_op
                    else:
                        i += 3
                elif opp_code == 6:
                    l_op = codes[i+1]
                    r_op = codes[i+2]
                    if len(par_modes) >= 1:
                        if par_modes[0] == 1:
                            l_op = codes[i+1]
                        elif par_modes[0] == 0:
                            l_op = codes[codes[i+1]]
                        else:
                            print('OPP CODE 2 ERROR')
                            exit(1)
                    if len(par_modes) >= 2:
                        if par_modes[1] == 1:
                            r_op = codes[i+2]
                        elif par_modes[1] == 0:
                            r_op = codes[codes[i+2]]
                        else:
                            print('OPP CODE 6 ERROR')
                            exit(1)
                    else:
                        r_op = codes[codes[i+2]]
                    if l_op == 0:
                        i = r_op
                    else:
                        i += 3
                elif opp_code == 7:
                    l_op = codes[i+1]
                    r_op = codes[i+2]
                    if len(par_modes) >= 1:
                        if par_modes[0] == 1:
                            l_op = codes[i+1]
                        elif par_modes[0] == 0:
                            l_op = codes[codes[i+1]]
                        else:
                            print('OPP CODE 7 ERROR')
                            exit(1)
                    if len(par_modes) >= 2:
                        if par_modes[1] == 1:
                            r_op = codes[i+2]
                        elif par_modes[1] == 0:
                            r_op = codes[codes[i+2]]
                        else:
                            print('OPP CODE 7 ERROR')
                            exit(1)
                    else:
                        r_op = codes[codes[i+2]]
                    if l_op < r_op:
                        codes[codes[i+3]] = 1
                    else:
                        codes[codes[i+3]] = 0
                    i += 4
                elif opp_code == 8:
                    l_op = codes[i+1]
                    r_op = codes[i+2]
                    if len(par_modes) >= 1:
                        if par_modes[0] == 1:
                            l_op = codes[i+1]
                        elif par_modes[0] == 0:
                            l_op = codes[codes[i+1]]
                        else:
                            print('OPP CODE 8 ERROR')
                            exit(1)
                    if len(par_modes) >= 2:
                        if par_modes[1] == 1:
                            r_op = codes[i+2]
                        elif par_modes[1] == 0:
                            r_op = codes[codes[i+2]]
                        else:
                            print('OPP CODE 8 ERROR')
                            exit(1)
                    else:
                        r_op = codes[codes[i+2]]
                    if l_op == r_op:
                        codes[codes[i+3]] = 1
                    else:
                        codes[codes[i+3]] = 0
                    i += 4
                elif opp_code == 99:
                    print('HALT')
                    break
            amp_index += 1   

        t = (perm, amp_output_signal[-1])
        total.append(t)    

    # now go through total and find the highest thruse value 
    highest = total[0]
    for t in total:
        if t[1] > highest[1]:
            highest = t

    print("HIGHEST THRUST FOUND: {} AMP CONFIG WITH {} THRUST".format(highest[0], highest[1]))

if __name__ == "__main__":
    perms = [''.join(p) for p in permutations('01234')]
    main(perms)                
