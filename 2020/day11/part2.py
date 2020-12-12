from IPython import embed as shell
import numpy as np
import sys

lines = [f.replace('\n','') for f in open(sys.argv[1], 'r').readlines()]

print('dimensions: {}x{}'.format(len(lines), len(lines[0])))

curr_count = sum([line.count('L') for line in lines])

prev_count = -1

for line in lines:
    print(line)

while curr_count != prev_count:

    new_seats = lines.copy()
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if i == 0 and j == 0: # upper left corner
                adj = ''
                
                a = i+1
                while a < len(lines): # down direction
                    if lines[a][j] == '.':
                        a += 1
                        continue
                    adj += lines[a][j]
                    break

                a = i+1
                b = j+1
                while a < len(lines) and b < len(lines[i]): # lower right direction
                    if lines[a][b] == '.':
                        a += 1
                        b += 1
                        continue
                    adj += lines[a][b]
                    break

                b = j+1
                while b < len(lines[i]): # right direction
                    if lines[i][b] == '.':
                        b += 1
                        continue
                    adj += lines[i][b]
                    break                

                occs = adj.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 5:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            elif (i == 0) and (j == (len(lines[i]) - 1)): # upper right corner
                #amt = lines[i+1][j] + lines[i+1][j-1] + lines[i][j-1]
                
                adj = ''
                a = i+1
                while a < len(lines): # down direction
                    if lines[a][j] == '.':
                        a += 1
                        continue
                    adj += lines[a][j]
                    break
                a = i+1
                b = j-1
                while a < len(lines) and b >= 0: # lower left diag
                    if lines[a][b] == '.':
                        a += 1
                        b += -1
                        continue
                    adj += lines[a][b]
                    break

                b = j-1
                while b >= 0: # left direction
                    if lines[i][b] == '.':
                        b += -1
                        continue
                    adj += lines[i][b]
                    break


                occs = adj.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 5:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            elif (j == 0) and (i == (len(lines) - 1)): # lower left corner
                #amt = lines[i-1][j] + lines[i-1][j+1] + lines[i][j+1]
                
                adj = ''
                a = i-1
                while a >= 0: # up direction
                    if lines[a][j] == '.':
                        a += -1
                        continue
                    adj += lines[a][j]
                    break

                a = i-1
                b = j+1
                while a >= 0 and b < len(lines[i]): # upper right diag
                    if lines[a][b] == '.':
                        a += -1
                        b += 1
                        continue
                    adj += lines[a][b]
                    break

                b = j+1
                while b < len(lines[i]): # right direction
                    if lines[i][b] == '.':
                        b += 1
                        continue
                    adj += lines[i][b]
                    break

                occs = adj.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 5:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            elif (j == (len(lines[i]) - 1) and (i == (len(lines) - 1))): # lower right corner
                #amt = lines[i][j-1] + lines[i-1][j-1] + lines[i-1][j]
                
                adj = ''
                a = i-1
                while a >= 0: # up direction
                    if lines[a][j] == '.':
                        a += -1
                        continue
                    adj += lines[a][j]
                    break

                a = i-1
                b = j-1
                while a >= 0 and b >= 0: # upper left diag
                    if lines[a][b] == '.':
                        a += -1
                        b += -1
                        continue
                    adj += lines[a][b]
                    break

                b = j-1
                while b >= 0: # left direction
                    if lines[i][b] == '.':
                        b += -1
                        continue
                    adj += lines[i][b]
                    break

                occs = adj.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 5:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            elif i == 0: # top row
                adj = ''
                b = j-1
                while b >= 0: # left direction
                    if lines[i][b] == '.':
                        b += -1
                        continue
                    adj += lines[i][b]
                    break

                a = i+1
                b = j-1
                while b >= 0 and a < len(lines): # lower left diag
                    if lines[a][b] == '.':
                        a += 1
                        b += -1
                        continue
                    adj += lines[a][b]
                    break

                a = i
                while a < len(lines): # down direction
                    if lines[a][j] == '.':
                        a += 1
                        continue
                    adj += lines[a][j]
                    break

                a = i+1
                b = j+1
                while b < len(lines[i]) and a < len(lines): # lower right diag
                    if lines[a][b] == '.':
                        a += 1
                        b += 1
                        continue
                    adj += lines[a][b]
                    break 

                b = j+1
                while b < len(lines[i]): # right direction
                    if lines[i][b] == '.':
                        b += 1
                        continue
                    adj += lines[i][b]
                    break


                #amt = lines[i][j-1] + lines[i+1][j-1] + lines[i+1][j] + lines[i+1][j+1] + lines[i][j+1]
                occs = adj.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 5:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            elif i == len(lines) - 1: # bottom row
                #amt = lines[i][j-1] + lines[i-1][j-1] + lines[i-1][j] + lines[i-1][j+1] + lines[i][j+1]
                adj = ''
                b = j-1
                while b >= 0: # left direction
                    if lines[i][b] == '.':
                        b += -1
                        continue
                    adj += lines[i][b]
                    break

                a = i-1
                b = j-1
                while b >= 0 and a >= 0: # upper left diagonal
                    if lines[a][b] == '.':
                        a += -1
                        b += -1
                        continue
                    adj += lines[a][b]
                    break

                a = i-1
                while a >= 0: # upwards direction
                    if lines[a][j] == '.':
                        a += -1
                        continue
                    adj += lines[a][j]
                    break

                a = i-1
                b = j+1
                while b < len(lines[i]) and a >= 0: # upper right diag
                    if lines[a][b] == '.':
                        a += -1
                        b += 1
                        continue
                    adj += lines[a][b]
                    break 

                b = j+1
                while b < len(lines[i]): # right direction
                    if lines[i][b] == '.':
                        b += 1
                        continue
                    adj += lines[i][b]
                    break

                occs = adj.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 5:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            elif j == 0: # left column
                #amt = lines[i-1][j] + lines[i-1][j+1] + lines[i][j+1] + lines[i+1][j+1] + lines[i+1][j]
                
                adj = ''
                a = i-1
                while a >= 0: # upwards direction
                    if lines[a][j] == '.':
                        a += -1
                        continue
                    adj += lines[a][j]
                    break

                a = i-1
                b = j+1
                while b < len(lines[i]) and a >= 0: # upper right diag
                    if lines[a][b] == '.':
                        a += -1
                        b += 1
                        continue
                    adj += lines[a][b]
                    break

                b = j+1
                while b < len(lines[i]): # right direction
                    if lines[i][b] == '.':
                        b += 1
                        continue
                    adj += lines[i][b]
                    break

                a = i+1
                b = j+1
                while b < len(lines[i]) and a < len(lines): # lower right diag
                    if lines[a][b] == '.':
                        a += 1
                        b += 1
                        continue
                    adj += lines[a][b]
                    break

                a = i+1
                while a < len(lines): # down direction
                    if lines[a][j] == '.':
                        a += 1
                        continue
                    adj += lines[a][j]
                    break

                occs = adj.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 5:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            elif j == len(lines[i]) - 1: # right column
                #amt = lines[i+1][j] + lines[i+1][j-1] + lines[i][j-1] + lines[i-1][j-1] + lines[i-1][j]
                adj = ''

                a = i-1
                while a >= 0: # upwards direction
                    if lines[a][j] == '.':
                        a += -1
                        continue
                    adj += lines[a][j]
                    break

                a = i-1
                b = j-1
                while b >= 0 and a >= 0: # upper left diagonal
                    if lines[a][b] == '.':
                        a += -1
                        b += -1
                        continue
                    adj += lines[a][b]
                    break

                b = j-1
                while b >= 0: # left direction
                    if lines[i][b] == '.':
                        b += -1
                        continue
                    adj += lines[i][b]
                    break

                a = i+1
                b = j-1
                while b >= 0 and a < len(lines): # lower left diag
                    if lines[a][b] == '.':
                        a += 1
                        b += -1
                        continue
                    adj += lines[a][b]
                    break

                a = i+1
                while a < len(lines): # down direction
                    if lines[a][j] == '.':
                        a += 1
                        continue
                    adj += lines[a][j]
                    break


                occs = adj.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 5:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            else: # everyone else
                adj = ''
                #amt = lines[i-1][j-1] + lines[i-1][j] + lines[i-1][j+1] + lines[i][j+1] + lines[i+1][j+1] + lines[i+1][j] + lines[i+1][j-1] + lines[i][j-1]
                
                a = i-1
                while a >= 0: # upwards direction
                    if lines[a][j] == '.':
                        a += -1
                        continue
                    adj += lines[a][j]
                    break

                a = i-1
                b = j+1
                while b < len(lines[i]) and a >= 0: # upper right diag
                    if lines[a][b] == '.':
                        a += -1
                        b += 1
                        continue
                    adj += lines[a][b]
                    break
                    
                b = j+1
                while b < len(lines[i]): # right direction
                    if lines[i][b] == '.':
                        b += 1
                        continue
                    adj += lines[i][b]
                    break

                a = i+1
                b = j+1
                while b < len(lines[i]) and a < len(lines): # lower right diag
                    if lines[a][b] == '.':
                        a += 1
                        b += 1
                        continue
                    adj += lines[a][b]
                    break

                a = i+1
                while a < len(lines): # down direction
                    if lines[a][j] == '.':
                        a += 1
                        continue
                    adj += lines[a][j]
                    break

                a = i+1
                b = j-1
                while b >= 0 and a < len(lines): # lower left diag
                    if lines[a][b] == '.':
                        a += 1
                        b += -1
                        continue
                    adj += lines[a][b]
                    break

                b = j-1
                while b >= 0: # left direction
                    if lines[i][b] == '.':
                        b += -1
                        continue
                    adj += lines[i][b]
                    break

                a = i-1
                b = j-1
                while b >= 0 and a >= 0: # upper left diagonal
                    if lines[a][b] == '.':
                        a += -1
                        b += -1
                        continue
                    adj += lines[a][b]
                    break

                occs = adj.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 5:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

    prev_count = curr_count
    curr_count = sum([new_seat.count('L') for new_seat in new_seats])
    lines = new_seats

    print('------------------------------------')
    for line in lines:
        print(line)
    #shell()


print(sum([new_seat.count('#') for new_seat in new_seats]))

