import sys
import numpy as np

from IPython import embed as shell

f = open(sys.argv[1], 'r')

target = sys.argv[2]
codes = []
for a in range(0,99):
	for b in range(0,99):
		f = open(sys.argv[1], 'r')
		codes = f.read().replace('\n', '').split(',')

		#shell()
		codes = np.array(codes, dtype='int32')

		codes[1] = a
		codes[2] = b

		i=0
		while i < len(codes):
			if codes[i] == 1:
				codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
				i += 4
			elif codes[i] == 2:
				codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
				i += 4
			elif codes[i] == 99:
				break
				
		if codes[0] == int(target):
			print('answer: {}'.format(100*codes[1]+codes[2]))
			exit(0)


#print(codes)
