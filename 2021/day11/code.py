import numpy as np

#### Read Data from txt file
#### and put in list named Data

file = open('data.txt', 'r')
raw_text = file.readlines()

n = len(raw_text)

# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.

def corrupt_line(string):
    collapsed = []
    corrupted = 0
    for i in range(len(string)):
        if string[i] in ['(', '[', '{', '<']:
            collapsed.append(string[i])
        elif len(string) == 0:
            corrupted = string[i]
        else:
            if string[i] == ')' and collapsed[-1] == '(':
                collapsed.pop(-1)
            elif string[i] == ']' and collapsed[-1] == '[':
                collapsed.pop(-1)
            elif string[i] == '}' and collapsed[-1] == '{':
                collapsed.pop(-1)
            elif string[i] == '>' and collapsed[-1] == '<':
                collapsed.pop(-1)
            else:
                corrupted = string[i]
        if corrupted != 0:
            if corrupted == ')':
                return 3
            if corrupted == ']':
                return 57
            if corrupted == '}':
                return 1197
            if corrupted == '>':
                return 25137
    return corrupted
            
        
    
count = 0
for i in range(n):
    string = raw_text[i].split()[0]
    count += corrupt_line(string)

print('Answer for Day 9 Part 1 is:', count)

def complete_line(string):
    collapsed = []
    score = 0
    for i in range(len(string)):
        if string[i] in ['(', '[', '{', '<']:
            collapsed.append(string[i])
        else:
            if string[i] == ')' and collapsed[-1] == '(':
                collapsed.pop(-1)
            elif string[i] == ']' and collapsed[-1] == '[':
                collapsed.pop(-1)
            elif string[i] == '}' and collapsed[-1] == '{':
                collapsed.pop(-1)
            elif string[i] == '>' and collapsed[-1] == '<':
                collapsed.pop(-1)
    while (collapsed != []):
        score *= 5
        if collapsed[-1] == '(':
            score += 1
        elif collapsed[-1] == '[':
            score += 2
        elif collapsed[-1] == '{':
            score += 3
        elif collapsed[-1] == '<':
            score += 4
        collapsed.pop(-1)
    return score
        
scores = []
for i in range(n):
    string = raw_text[i].split()[0]
    if corrupt_line(string) == 0:
        scores.append(complete_line(string))
            
mid = int((len(scores) - 1)/2)

print('Answer for Day 9 Part 2 is:', sorted(scores)[mid])   
