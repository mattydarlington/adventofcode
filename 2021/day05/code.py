import numpy as np

#### Read Data from txt file
#### and put in list named Data
file = open('data.txt', 'r')
raw_text = file.readlines()
n = len(raw_text)

x1 = []
y1 = []
x2 = []
y2 = []
for i in range(n):
    x1.append(int(raw_text[i].split()[0].split(',')[0]))
    y1.append(int(raw_text[i].split()[0].split(',')[1]))
    x2.append(int(raw_text[i].split()[2].split(',')[0]))
    y2.append(int(raw_text[i].split()[2].split(',')[1]))
    
x_len = max(set(x1).union(set(x2)))+1
y_len = max(set(y1).union(set(y2)))+1

grid = np.zeros((x_len, y_len))

### Add horizontal and vertical pipes

for i in range(n):
    if x1[i] == x2[i]:
        start = min(y1[i], y2[i])
        end = max(y1[i], y2[i])+1
        for j in range(start,end):
            grid[x1[i],j] += 1
    elif y1[i] == y2[i]:
        start = min(x1[i], x2[i])
        end = max(x1[i], x2[i])+1
        for j in range(start,end):
            grid[j,y1[i]] += 1
    
print('Answer for Day 5 Part 1 is:', np.sum(grid >= 2))

### Add diagonal pipes

for i in range(n):
    if x1[i] != x2[i] and y1[i] != y2[i]:
        length = abs(x1[i] - x2[i]) + 1
        x_dir = int( (x2[i] - x1[i]) / abs(x1[i] - x2[i]) )
        y_dir = int( (y2[i] - y1[i]) / abs(y1[i] - y2[i]) )
        for j in range(length):
            grid[x1[i] + j*x_dir, y1[i] + j*y_dir] += 1

print('Answer for Day 5 Part 2 is:', np.sum(grid >= 2))   
