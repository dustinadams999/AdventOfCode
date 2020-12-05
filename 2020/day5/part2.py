"""
usage: $ python part2.py <input-file>
"""
import sys

f = open(sys.argv[1],'r')

highest = 0
seats = []
for i in f.readlines():
    row = i[:7].replace('F', '0')
    row = row.replace('B', '1')
    row_num = int(row[0])*pow(2,6)+int(row[1])*pow(2,5)+int(row[2])*pow(2,4)+int(row[3])*pow(2,3)+int(row[4])*pow(2,2)+int(row[5])*pow(2,1)+int(row[6])*pow(2,0)
    
    col = i[-4:].replace('R', '1')
    col = col.replace('L', '0')
    col_num = int(col[0])*pow(2,2)+int(col[1])*pow(2,1)+int(col[2])*pow(2,0)
    seat_num = row_num*8 + col_num

    seats.append(seat_num)

seats.sort()

for i in range(0,len(seats)-1):
    if seats[i+1] != seats[i]+1:
        print('between seats {} and {}'.format(seats[i], seats[i+1]))
