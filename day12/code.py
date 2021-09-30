import copy
#### Reads data
file = open('data.txt', 'r')
raw_text = file.readlines()
n = len(raw_text)
for i in range(n):
    raw_text[i] = raw_text[i].strip()
    
### Action N means to move north by the given value.
### Action S means to move south by the given value.
### Action E means to move east by the given value.
### Action W means to move west by the given value.
### Action L means to turn left the given number of degrees.
### Action R means to turn right the given number of degrees.
### Action F means to move forward by the given value in the direction the ship is currently facing.
    
def move(x, y, bearing, instruction):
    letter = instruction[0]
    number = int(instruction[1:])
    
    if letter == 'N':
        x += number        
    if letter == 'S':
        x -= number        
    if letter == 'E':
        y += number        
    if letter == 'W':
        y -= number        
    
    if letter == 'L':
        bearing -= number        
        bearing = bearing%360
    if letter == 'R':
        bearing += number    
        bearing = bearing%360
    
    if letter == 'F':
        if bearing == 0:
            x += number        
        if bearing == 90:
            y += number        
        if bearing == 180:
            x -= number        
        if bearing == 270:
            y -= number     
        
    return x, y, bearing
    
def simulate(instructions):
    x = 0
    y = 0
    bearing = 90
    n = len(instructions)
    for i in range(n):
        x, y, bearing = move(x, y, bearing, instructions[i])
    return x, y, bearing

def distance(x, y):
    return abs(x) + abs(y)

x, y = simulate(raw_text)[:2]
answer = distance(x,y)
    
print('Answer for Day 12 Part 1 is:', answer)  

### Action N means to move the waypoint north by the given value.
### Action S means to move the waypoint south by the given value.
### Action E means to move the waypoint east by the given value.
### Action W means to move the waypoint west by the given value.
### Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
### Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
### Action F means to move forward to the waypoint a number of times equal to the given value.
### Waypoint starts at (1, 10)
    
def move2(ship_x, ship_y, way_x, way_y, instruction):
    letter = instruction[0]
    number = int(instruction[1:])
    
    if letter == 'N':
        way_y += number
    if letter == 'S':  
        way_y -= number       
    if letter == 'E':   
        way_x += number       
    if letter == 'W':    
        way_x -= number       
    
    if letter == 'L':
        x = way_x - ship_x
        y = way_y - ship_y
        for i in range(int(number/90)):
            x = way_x - ship_x
            y = way_y - ship_y
            x_temp = -y
            y_temp = x
            way_x = ship_x + x_temp
            way_y = ship_y + y_temp
    
    
    if letter == 'R':
        for i in range(int(number/90)):
            x = way_x - ship_x
            y = way_y - ship_y
            x_temp = y
            y_temp = -x
            way_x = ship_x + x_temp
            way_y = ship_y + y_temp
    
    if letter == 'F':
        for i in range(number):
            x = way_x - ship_x
            ship_x += x
            way_x += x
            y = way_y - ship_y
            ship_y += y
            way_y += y
            
    return ship_x, ship_y, way_x, way_y

def simulate2(instructions):
    ship_x = 0
    ship_y = 0
    way_x = 10
    way_y = 1
    n = len(instructions)
    for i in range(n):
        ship_x, ship_y, way_x, way_y = move2(ship_x, ship_y, way_x, way_y, instructions[i])
    return ship_x, ship_y, way_x, way_y
    
x, y = simulate2(raw_text)[:2]
answer = distance(x,y)

print('Answer for Day 12 Part 2 is:', answer)  
