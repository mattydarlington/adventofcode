import numpy as np

#### Read Data from txt file
#### and put in list named Data

file = open('data.txt', 'r')
raw_text = file.readlines()

n = len(raw_text)
m = len(raw_text[0]) - 1

grid = np.zeros((n,m))
for i in range(n):
    for j in range(m):
        grid[i,j] = int(raw_text[i][j])

count = 0
sinks = []
for i in range(n):
    for j in range(m):
        adj_greater = 0
        if i > 0:
            if grid[i,j] >= grid[i-1,j]:
                adj_greater += 1
        if i < n - 1:
            if grid[i,j] >= grid[i+1,j]:
                adj_greater += 1
        if j > 0:
            if grid[i,j] >= grid[i,j-1]:
                adj_greater += 1
        if j < m - 1:
            if grid[i,j] >= grid[i,j+1]:
                adj_greater += 1
        if adj_greater == 0:
            count += grid[i,j] + 1
            sinks.append([i,j])

print('Answer for Day 9 Part 1 is:', count)
    
basins = [0] * len(sinks)

for i in range(len(sinks)):
    area = [sinks[i]]
    running = 1
    while (running == 1):
        old_area = area.copy()
        for x in area:
            if x[0] > 0:
                if grid[x[0] - 1, x[1]] != 9:
                    if grid[x[0]-1, x[1]] >= grid[x[0], x[1]]:
                        if [x[0] - 1, x[1]] not in area:
                            area.append([x[0]-1, x[1]])
            if x[0] < n-1:
                if grid[x[0] + 1, x[1]] != 9:
                    if grid[x[0]+ 1, x[1]] >= grid[x[0], x[1]]:
                        if [x[0] + 1, x[1]] not in area:
                            area.append([x[0]+1, x[1]])
            if x[1] > 0:
                if grid[x[0],x[1]-1] != 9:
                    if grid[x[0], x[1]- 1] >= grid[x[0], x[1]]:
                        if [x[0], x[1]- 1] not in area:
                            area.append([x[0], x[1]- 1])
            if x[1] < m-1:
                if grid[x[0],x[1]+1] != 9:
                    if grid[x[0], x[1]+ 1] >= grid[x[0], x[1]]:
                        if [x[0], x[1]+ 1] not in area:
                            area.append([x[0], x[1]+ 1])
                        
         
            if x[0] == 1:
                if grid[x[0]- 1, x[1]] >= grid[x[0], x[1]]:
                    if [x[0] - 1, x[1]] not in area:
                        area.append([x[0]-1, x[1]])
            if x[0] == n-2:
                if grid[x[0]+ 1, x[1]] >= grid[x[0], x[1]]:
                    if [x[0] + 1, x[1]] not in area:
                        area.append([x[0]+1, x[1]])
            if x[1] == 1:
                if grid[x[0], x[1]- 1] >= grid[x[0], x[1]]:
                    if [x[0], x[1]- 1] not in area:
                        area.append([x[0], x[1]- 1])
            if x[1] == m-2:
                if grid[x[0], x[1]+ 1] >= grid[x[0], x[1]]:
                    if [x[0], x[1]+ 1] not in area:
                        area.append([x[0], x[1]+ 1])               
                        
                        
        if old_area == area:
            new_area = []
            for x in area:
                if grid[x[0],x[1]] != 9:
                    new_area.append(x)
            basins[i] = len(new_area)
            running = 0
        
print('Answer for Day 9 Part 2 is:', np.prod(sorted(basins)[-3:]))   
