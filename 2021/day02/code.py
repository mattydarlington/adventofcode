#### Read Data from txt file
#### and put in list named Data
file = open('data.txt', 'r')
raw_text = file.readlines()

direction = []
distance = []
n = len(raw_text)
for i in range(n):
    x = raw_text[i].split()
    direction.append(x[0])
    distance.append(int(x[1]))
    
### Find final co-ordinates and multiply them

horizontal = 0
depth = 0
for i in range(n):
    if direction[i] == 'forward':
        horizontal += distance[i]
    if direction[i] == 'down':
        depth += distance[i]
    if direction[i] == 'up':
        depth -= distance[i]
        
print('Answer for Day 2 Part 1 is:', depth * horizontal)

### Introduce Aim variable

horizontal = 0
depth = 0
aim = 0
for i in range(n):
    if direction[i] == 'forward':
        horizontal += distance[i]
        depth += aim * distance[i]
    if direction[i] == 'down':
        aim += distance[i]
    if direction[i] == 'up':
        aim -= distance[i]

print('Answer for Day 2 Part 2 is:', depth * horizontal)   
