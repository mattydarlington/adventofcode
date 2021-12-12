import numpy as np

#### Read Data from txt file
#### and put in list named Data

data = np.loadtxt('data.txt', delimiter = ',')

print('Answer for Day 7 Part 1 is:', sum(abs(data - np.median(data))))

def triangle(n):
    return n/2*(n+1)

def cost(crab, pos):
    return triangle(abs(crab-pos))

total_costs = np.zeros(int(max(data)))
for i in range(int(max(data))):
    for crab in data:
        total_costs[i] += cost(crab, i)
    

print('Answer for Day 7 Part 2 is:', min(total_costs))   
