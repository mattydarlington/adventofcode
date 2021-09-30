import copy
#### Reads data
file = open('data.txt', 'r')
raw_text = file.readlines()
n = len(raw_text)
for i in range(n):
    raw_text[i] = raw_text[i].strip()
m = len(raw_text[0])

#### Make 2d array of floor
floor = [''] * n
for i in range(n):
    floor[i] = [0] * m
for i in range(n):
    for j in range(m):
        floor[i][j] = raw_text[i][j]

#### Read seat status   
def seat_oc(layout, x, y):
    if layout[y][x] == '#':
        return 1
    else:
        return 0
def seat_em(layout, x, y):
    if layout[y][x] == 'L':
        return 1
    else:
        return 0
    
#### Calculate adjacent seat status
def adj_oc(layout, x, y):
    xlen = len(layout[0])
    ylen = len(layout)
    total = 0
    if x - 1 >= 0:
        total += seat_oc(layout, x - 1, y)
    if x + 1 <= xlen - 1:
        total += seat_oc(layout, x + 1, y)
    if y - 1 >= 0:
        total += seat_oc(layout, x,     y - 1)
    if y + 1 <= ylen - 1:
        total += seat_oc(layout, x,     y + 1)
    if x - 1 >= 0 and y - 1 >= 0:
        total += seat_oc(layout, x - 1, y - 1)
    if x - 1 >= 0 and y + 1 <= ylen - 1:
        total += seat_oc(layout, x - 1, y + 1)
    if x + 1 <= xlen - 1 and y - 1 >= 0:
        total += seat_oc(layout, x + 1, y - 1)
    if x + 1 <= xlen - 1 and y + 1 <= ylen - 1:
        total += seat_oc(layout, x + 1, y + 1)
    return total

#### Run Simulation
def simulate(layout):
    layout_old = copy.deepcopy(layout)
    layout_new = copy.deepcopy(layout)
    xlen = len(layout[0])
    ylen = len(layout)
    while(True):
        for x in range(xlen):
            for y in range(ylen):
                if seat_em(layout_old, x, y) == 1 and adj_oc(layout_old, x, y) == 0:
                    layout_new[y][x] = '#'
                elif seat_oc(layout_old, x, y) == 1 and adj_oc(layout_old, x, y) >= 4:
                    layout_new[y][x] = 'L'
        if layout_old == layout_new:
            return layout_new
        else:
            layout_old = copy.deepcopy(layout_new)

####
converged = simulate(floor)
total = 0
for x in range(m):
    for y in range(n):
        total += seat_oc(converged, x, y)
print('Answer for Day 11 Part 1 is:', total)  

#### Part Two
#### Look for next seat i.e. miss out floor from calcs
#### 1 if seat, 0 if floor, -1 if out of bounds
def seat_exist(layout, x, y):
    xlen = len(layout[0])
    ylen = len(layout)
    if 0 <= x <= xlen-1 and 0 <= y <= ylen - 1:
        if layout[y][x] == '.':
            return 0
        else:
            return 1
    else:
        return -1

#### Calculate adjacent seat status
def adj_oc(layout, x, y):
    xlen = len(layout[0])
    ylen = len(layout)
    total = 0
    
    i = 1
    while(i > 0):
        if seat_exist(layout, x + i, y) == -1:
            i = -1
        elif seat_exist(layout, x + i, y) == 0:
            i += 1
        else:
            total += seat_oc(layout, x + i , y)
            i = -1
            
    i = 1
    while(i > 0):
        if seat_exist(layout, x - i, y) == -1:
            i = -1
        elif seat_exist(layout, x - i, y) == 0:
            i += 1
        else:
            total += seat_oc(layout, x - i , y)
            i = -1
            
    i = 1
    while(i > 0):
        if seat_exist(layout, x, y + i) == -1:
            i = -1
        elif seat_exist(layout, x, y + i) == 0:
            i += 1
        else:
            total += seat_oc(layout, x, y + i)
            i = -1
            
    i = 1
    while(i > 0):
        if seat_exist(layout, x, y - i) == -1:
            i = -1
        elif seat_exist(layout, x, y - i) == 0:
            i += 1
        else:
            total += seat_oc(layout, x, y - i)
            i = -1
            
    i = 1
    while(i > 0):
        if seat_exist(layout, x + i, y + i) == -1:
            i = -1
        elif seat_exist(layout, x + i, y + i) == 0:
            i += 1
        else:
            total += seat_oc(layout, x + i , y + i)
            i = -1
            
    i = 1
    while(i > 0):
        if seat_exist(layout, x + i, y - i) == -1:
            i = -1
        elif seat_exist(layout, x + i, y - i) == 0:
            i += 1
        else:
            total += seat_oc(layout, x + i , y - i)
            i = -1
    i = 1
    while(i > 0):
        if seat_exist(layout, x - i, y + i) == -1:
            i = -1
        elif seat_exist(layout, x - i, y + i) == 0:
            i += 1
        else:
            total += seat_oc(layout, x - i , y + i)
            i = -1
            
    i = 1
    while(i > 0):
        if seat_exist(layout, x - i, y - i) == -1:
            i = -1
        elif seat_exist(layout, x - i, y - i) == 0:
            i += 1
        else:
            total += seat_oc(layout, x - i , y - i)
            i = -1
            
    return total

#### Run Simulation
def simulate(layout):
    layout_old = copy.deepcopy(layout)
    layout_new = copy.deepcopy(layout)
    xlen = len(layout[0])
    ylen = len(layout)
    while(True):
        for x in range(xlen):
            for y in range(ylen):
                if seat_em(layout_old, x, y) == 1 and adj_oc(layout_old, x, y) == 0:
                    layout_new[y][x] = '#'
                elif seat_oc(layout_old, x, y) == 1 and adj_oc(layout_old, x, y) >= 5:
                    layout_new[y][x] = 'L'
        if layout_old == layout_new:
            return layout_new
        else:
            layout_old = copy.deepcopy(layout_new)

####
converged = simulate(floor)
total = 0
for x in range(m):
    for y in range(n):
        total += seat_oc(converged, x, y)
print('Answer for Day 11 Part 2 is:', total)  