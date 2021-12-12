import numpy as np

#### Read Data from txt file
#### and put in list named Data
file = open('data.txt', 'r')
raw_text = file.readlines()

n = len(raw_text)

inputs = np.zeros((n, 10), dtype = "U7")
output = np.zeros((n, 4),  dtype = "U7")

for i in range(n):
    x, y = raw_text[i].split('|')
    for j in range(10):
        inputs[i][j] = x.split()[j]
    for j in range(4):
        output[i][j] = y.split()[j]
        
count = 0
for i in range(n):
    for j in range(4):
        if len(output[i][j]) in (2,3,4,7):
            count += 1

print('Answer for Day 8 Part 1 is:', count)

# Find the permutation from [a,b,c,d,e,f,g] to ?

count = 0
for i in range(n):
    
    ### Determine uncoding
    
    permutation = [0]*7
    for j in range(10):
        if len(inputs[i][j]) == 2:
            one = inputs[i][j]
        if len(inputs[i][j]) == 3:
            seven = inputs[i][j]
        if len(inputs[i][j]) == 4:
            four = inputs[i][j]
        if len(inputs[i][j]) == 7:
            eight = inputs[i][j]
            
    bd = set(four) - set(one)
    
    for j in range(10):
        if len(inputs[i][j]) == 6 and not set(one).issubset(set(inputs[i][j])):
            six = inputs[i][j]
        elif len(inputs[i][j]) == 6 and not bd.issubset(set(inputs[i][j])):
            zero = inputs[i][j]
        elif len(inputs[i][j]) == 6:
            nine = inputs[i][j]
    
    permutation[0] = set(seven) - set(one)
    permutation[2] = set(eight) - set(six)
    permutation[3] = set(eight) - set(zero)  
    permutation[4] = set(eight) - set(nine)
    permutation[5] = set(one) - set(permutation[2])
    
    for j in range(10):
        if len(inputs[i][j]) == 5 and set(one) <= set(inputs[i][j]):
            three = inputs[i][j]
            
    acdef = permutation[0] | permutation[2] | permutation[3] | permutation[4] | permutation[5]
    bg = set(eight) - acdef
    
    permutation[1] = bd & bg
    permutation[6] = bg - permutation[1]
    
    for j in range(10):
        if set(inputs[i][j]) == permutation[0] | permutation[2] | permutation[3] | permutation[4] | permutation[6]:
            two = inputs[i][j]
        if set(inputs[i][j]) == permutation[0] | permutation[1] | permutation[3] | permutation[5] | permutation[6]:
            five = inputs[i][j]
    
    numbers = [0]*4
    
    for j in range(4):
        if set(output[i][j]) == set(zero):
            numbers[j] = 0
        if set(output[i][j]) == set(one):
            numbers[j] = 1
        if set(output[i][j]) == set(two):
            numbers[j] = 2
        if set(output[i][j]) == set(three):
            numbers[j] = 3
        if set(output[i][j]) == set(four):
            numbers[j] = 4
        if set(output[i][j]) == set(five):
            numbers[j] = 5
        if set(output[i][j]) == set(six):
            numbers[j] = 6
        if set(output[i][j]) == set(seven):
            numbers[j] = 7
        if set(output[i][j]) == set(eight):
            numbers[j] = 8
        if set(output[i][j]) == set(nine):
            numbers[j] = 9
        count += numbers[j] * 10**(3-j)
    
print('Answer for Day 8 Part 2 is:', count)   
