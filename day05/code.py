#### Reads in data
file = open('data.txt', 'r')
raw_text = file.readlines()
n = len(raw_text)
for i in range(n):
    raw_text[i] = raw_text[i].strip()

#### Split rows and columns
row = []
column = []
for i in range(n):
    row.append(raw_text[i][:7])
    column.append(raw_text[i][7:])
    
#### Convert string to 0 and 1. 'F' and 'B' for row and 'L' and 'R' for column
row_bin = ['']*n
col_bin = ['']*n
for i in range(n):
    for j in range(7):
        if row[i][j] == 'F':
            row_bin[i] += '0'
        else:
            row_bin[i] += '1'
    for j in range(3):
        if column[i][j] == 'L':
            col_bin[i] += '0'
        else:
            col_bin[i] += '1'
            
#### Convert binary to decimal
row_no = []
col_no = []
for i in range(n):
    row_no.append(int(row_bin[i],2))
    col_no.append(int(col_bin[i],2))

#### Seat id is 8 times row number plus column number
seat_id = []
for i in range(n):
    seat_id.append(row_no[i]*8 + col_no[i])

#### Need to find max seat id
answer = max(seat_id)
print('Answer for Day 5 Part 1 is:', answer)

#### Find missing seat id in middle
seat_id = sorted(seat_id)
seat_one = min(seat_id)
for i in range(n):
    if i + seat_one != seat_id[i]:
        answer = seat_id[i] - 1
        break
    
print('Answer for Day 5 Part 2 is:', answer)
