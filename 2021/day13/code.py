import numpy as np

#### Read Data from txt file
#### and put in list named Data

file = open('data.txt', 'r')
raw_text = file.readlines()

n = len(raw_text)
x_coord = []
y_coord = []
fold_dir = []
fold_pos = []
space = 0
for i in range(n):
    if raw_text[i] == '\n':
        space = 1
    elif space == 0:
        x = raw_text[i].split()[0].split(',')
        x_coord.append(int(x[1]))
        y_coord.append(int(x[0]))
    else:
        x = raw_text[i].split()[2].split('=')
        fold_dir.append(x[0])
        fold_pos.append(int(x[1]))
       
n = 0
m = 0
k = len(fold_dir)
for i in range(k):
    if fold_dir[i] == 'x':
        m = max(2*fold_pos[i] + 1, m)
    if fold_dir[i] == 'y':
        n = max(2*fold_pos[i] + 1, n)
       
d = len(x_coord)

grid = np.zeros((n,m))
for i in range(d):
    grid[x_coord[i], y_coord[i]] = 1
    
def fold_x(grid):
    n, m = grid.shape
    new_m = int((m - 1)/2)
    new_grid = np.zeros((n, new_m))
    for i in range(n):
        for j in range(m):
            if grid[i,j] == 1:
                if j < new_m:
                    new_grid[i,j] = 1
                if j == new_m:
                    print('error')
                if j > new_m:
                    new_grid[i, 2*new_m - j] = 1
                               
    return new_grid

def fold_y(grid):
    return np.rot90(fold_x(np.rot90(grid, k = 1)), k=3)

import seaborn as sns
import matplotlib.pyplot as plt
for i in range(1):
    sns.heatmap(grid)
    plt.show()
    if fold_dir[i] == 'x':
        grid = fold_x(grid)
    if fold_dir[i] == 'y':
        grid = fold_y(grid)
sns.heatmap(grid)

print('Answer for Day 13 Part 1 is:', np.sum(grid))

for i in range(1,len(fold_dir)):
    sns.heatmap(grid)
    plt.show()
    if fold_dir[i] == 'x':
        grid = fold_x(grid)
    if fold_dir[i] == 'y':
        grid = fold_y(grid)
sns.heatmap(grid)

print('Answer for Day 13 Part 2 is:', 'see plot')   