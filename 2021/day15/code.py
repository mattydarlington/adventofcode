import numpy as np

#### Read Data from txt file
#### and put in list named Data

file = open('data.txt', 'r')
raw_text = file.readlines()

n = len(raw_text)
m = len(raw_text[0])-1

grid = np.zeros((n,m))

for i in range(n):
    for j in range(m):
        grid[i,j] = int(raw_text[i][j])

# Gets value of neighbours
def val_neigh(grid, V, x, y):
    n, m = grid.shape
    vals = []
    if x != n-1:
        vals.append(grid[x+1,y] + V[x+1,y])
    if y != m-1:
        vals.append(grid[x,y+1] + V[x,y+1])
    if x == y == n-1:
        vals.append(0)
    return vals

# Value of square is shortest path to end
V = np.ones((n,m))        

for k in range(n+m-1, -1, -1):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                V[i,j] = np.min(val_neigh(grid, V, i, j))

print('Answer for Day 15 Part 1 is:', V[0,0])

### Repeat map 5 times in each direction. Each repetition increases risk by 1.
### Risk of 9 wraps around to 1

grid_5 = np.zeros((5*n, 5*m))

for i in range(n):
    for j in range(m):
        for k1 in range(5):
            for k2 in range(5):
                if k1+k2+grid[i,j] < 10:
                    grid_5[k1*n + i,k2*m + j] = k1+k2+grid[i,j]
                else:
                    grid_5[k1*n + i,k2*m + j] = (k1+k2+grid[i,j])%10 + 1
   
import networkx as nx
G = nx.DiGraph()
for i in range(5*n-1):
    for j in range(5*m-1):
        G.add_edge((i,j), (i+1,j), weight = grid_5[i+1,j])
        G.add_edge((i,j), (i,j+1), weight = grid_5[i,j+1])
        
for i in range(5*n-1):
    G.add_edge((499,i), (499,i+1), weight = grid_5[49, i+1])
    G.add_edge((i,499), (i+1,499), weight = grid_5[i+1, 49])
        
print('Answer for Day 15 Part 2 is:', nx.shortest_path_length(G, (0,0), (499,499), weight = 'weight'))   