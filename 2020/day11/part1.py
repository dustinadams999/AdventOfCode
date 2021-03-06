import sys

lines = [f.replace('\n','') for f in open(sys.argv[1], 'r').readlines()]

print('dimensions: {}x{}'.format(len(lines), len(lines[0])))

curr_count = sum([line.count('L') for line in lines])

prev_count = -1

while curr_count != prev_count:

    new_seats = lines.copy()
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if i == 0 and j == 0: # upper left corner
                amt = lines[i][j+1] + lines[i+1][j+1] + lines[i+1][j]
                occs = amt.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                        #new_seats[i][j] = '#'
                elif lines[i][j] == '#':
                    if occs >= 4:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            elif (i == 0) and (j == (len(lines[i]) - 1)): # upper right corner
                amt = lines[i+1][j] + lines[i+1][j-1] + lines[i][j-1]
                occs = amt.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 4:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            elif (j == 0) and (i == (len(lines) - 1)): # lower left corner
                amt = lines[i-1][j] + lines[i-1][j+1] + lines[i][j+1]
                occs = amt.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 4:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            elif (j == (len(lines[i]) - 1) and (i == (len(lines) - 1))): # lower right corner
                amt = lines[i][j-1] + lines[i-1][j-1] + lines[i-1][j]
                occs = amt.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 4:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            elif i == 0: # top row
                amt = lines[i][j-1] + lines[i+1][j-1] + lines[i+1][j] + lines[i+1][j+1] + lines[i][j+1]
                occs = amt.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 4:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            elif i == len(lines) - 1: # bottom row
                amt = lines[i][j-1] + lines[i-1][j-1] + lines[i-1][j] + lines[i-1][j+1] + lines[i][j+1]
                occs = amt.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 4:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            elif j == 0: # left column
                amt = lines[i-1][j] + lines[i-1][j+1] + lines[i][j+1] + lines[i+1][j+1] + lines[i+1][j]
                occs = amt.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 4:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            elif j == len(lines[i]) - 1: # right column
                amt = lines[i+1][j] + lines[i+1][j-1] + lines[i][j-1] + lines[i-1][j-1] + lines[i-1][j]
                occs = amt.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 4:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

            else: # everyone else
                amt = lines[i-1][j-1] + lines[i-1][j] + lines[i-1][j+1] + lines[i][j+1] + lines[i+1][j+1] + lines[i+1][j] + lines[i+1][j-1] + lines[i][j-1]
                occs = amt.count('#')
                if lines[i][j] == 'L':
                    if occs == 0:
                        new_seats[i] = new_seats[i][0:j] + '#' + new_seats[i][j+1:]
                elif lines[i][j] == '#':
                    if occs >= 4:
                        new_seats[i] = new_seats[i][0:j] + 'L' + new_seats[i][j+1:]

    prev_count = curr_count
    curr_count = sum([new_seat.count('L') for new_seat in new_seats])
    lines = new_seats

print(sum([new_seat.count('#') for new_seat in new_seats]))

