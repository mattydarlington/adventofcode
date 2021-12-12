import numpy as np

#### Read Data from txt file
#### and put in list named Data
file = open('data.txt', 'r')
raw_text = file.readlines()

fish_state = []
for fish in raw_text[0].split(','):
    fish_state.append(int(fish))
    
def simulate_fish(fish_state, days):
    fish_state = fish_state.copy()
    for i in range(days):
        n = len(fish_state)
        for j in range(n):
            if fish_state[j] == 0:
                fish_state[j] = 6
                fish_state.append(8)
            else:
                fish_state[j] = fish_state[j] - 1
    return fish_state

print('Answer for Day 6 Part 1 is:', len(simulate_fish(fish_state,80)))

# Need a smarter way for day 2
# Solve with recursion and cache the outputs

import functools

@functools.lru_cache(maxsize=None)
def num_fish(fish_state, days):
    if days == 0:
        return 1
    if fish_state == 0:
        return num_fish(6, days - 1) + num_fish(8, days - 1)
    else:
        return num_fish(fish_state - 1, days - 1)

total_fish = 0
for fish in fish_state:
    total_fish += num_fish(fish, 256)

print('Answer for Day 6 Part 2 is:', total_fish)   
