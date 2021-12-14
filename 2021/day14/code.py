import numpy as np

#### Read Data from txt file
#### and put in list named Data

file = open('data.txt', 'r')
raw_text = file.readlines()

n = len(raw_text) - 2

polymer = list(raw_text[0].split()[0])

pair = []
insert = []
for i in range(n):
    x = raw_text[i+2].split()
    pair.append(x[0])
    insert.append(x[2])
    
def step_polymer(polymer, pair, insert):
    n = len(pair)
    pointer = 0
    while (pointer < len(polymer)-1):
        p = pointer
        for i in range(n):
            if pair[i] == ''.join(polymer[pointer:pointer+2]) and p == pointer:
                polymer.insert(pointer+1, insert[i])
                pointer += 1
        pointer += 1
    return polymer                

for i in range(10):
    polymer = step_polymer(polymer, pair, insert)

counts = []
for char in insert:
    counts.append(polymer.count(char))

print('Answer for Day 14 Part 1 is:', max(counts)-min(counts))

### Looked at https://github.com/Leftfish/Advent-of-Code-2021/blob/main/14/d14.py for help

polymer = list(raw_text[0].split()[0])

from collections import defaultdict
pair_counts = defaultdict(lambda: 0)
for i in range(len(polymer)-1):
    string = polymer[i] + polymer[i+1]
    pair_counts[string] += 1

mapping = {}
for i in range(n):
    mapping[pair[i]] = insert[i]

char_counts = defaultdict(lambda: 0)
for char in polymer:
    char_counts[char] += 1

for i in range(40):
    new_counts = []
    for pair, count in pair_counts.items():
        new_char = mapping[pair]
        first_string = pair[0] + new_char
        second_string = new_char + pair[1]
        new_counts.append((first_string, count))
        new_counts.append((second_string, count))
        char_counts[new_char] += count
    pair_counts = defaultdict(lambda : 0)
    for pair, count in new_counts:
        pair_counts[pair] += count


most_char = max(char_counts.keys(), key=(lambda k: char_counts[k]))
least_char = min(char_counts.keys(), key=(lambda k: char_counts[k]))

print('Answer for Day 14 Part 2 is:', char_counts[most_char] - char_counts[least_char])   