import sys

f = open(sys.argv[1],'r')

highest = 0
for i in f.readlines():
    row = i[:7].replace('F', '0')
    row = row.replace('B', '1')
    row_num = int(row[0])*pow(2,6)+int(row[1])*pow(2,5)+int(row[2])*pow(2,4)+int(row[3])*pow(2,3)+int(row[4])*pow(2,2)+int(row[5])*pow(2,1)+int(row[6])*pow(2,0)
    
    col = i[-4:].replace('R', '1')
    col = col.replace('L', '0')
    #print('col: {}'.format(col))
    col_num = int(col[0])*pow(2,2)+int(col[1])*pow(2,1)+int(col[2])*pow(2,0)

    #print('row_num: {}, col_num: {}'.format(row_num, col_num))

    seat_num = row_num*8 + col_num

    if seat_num > highest:
        highest = seat_num



print(highest)