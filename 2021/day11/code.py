import numpy as np

#### Read Data from txt file
#### and put in list named Data

file = open('test_data.txt', 'r')
raw_text = file.readlines()

n = len(raw_text)
state = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        state[i][j] = raw_text[i][j]        
        
### Count no of flashes for 100 days
### Flash at 1 if 'about to flash' or at 2 if has flashed
        
def simulate_step(s_0):
    state = s_0.copy()
    n = len(state[0])
    for i in range(n):
        for j in range(n):
            state[i][j] += 1
        
    flash = np.zeros((n,n))
    while(True):
        flash_old = flash.copy()
        for i in range(n):
            for j in range(n):
                if state[i][j] > 9 and flash[i][j] == 0:
                    flash[i][j] = 1
                    state[i][j] += 1
        for i in range(n):
            for j in range(n):
                if flash[i][j] == 1:
                    if i > 0:
                        state[i-1][j] += 1
                        if j > 0:
                            state[i-1][j-1] += 1
                        if j < n-1:
                            state[i-1][j+1] += 1
                    if i < n-1:
                        state[i+1][j] += 1
                        if j > 0:
                            state[i+1][j-1] += 1
                        if j < n-1:
                            state[i+1][j+1] += 1
                    if j > 0:
                        state[i][j-1] += 1
                    if j < n-1:
                        state[i][j+1] += 1
                    flash[i][j] = 2
        if np.all(flash_old == flash):
            for i in range(n):
                for j in range(n):
                    if state[i][j] > 9:
                        state[i][j] = 0
            return state, np.sum(flash != 0)
        
count = 0
for i in range(100):
    state, n = simulate_step(state)
    count += n

print('Answer for Day 11 Part 1 is:', count)

### Find first day when all flash

file = open('data.txt', 'r')
raw_text = file.readlines()

n = len(raw_text)
state = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        state[i][j] = raw_text[i][j]      
        
days = 0
flashed = 0
states = []
while(flashed != n**2):
    state, flashed = simulate_step(state)
    states.append(state)
    days += 1

print('Answer for Day 11 Part 2 is:', days)   
