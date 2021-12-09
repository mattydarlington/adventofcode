#### Reads data
file = open('data.txt', 'r')
raw_text = file.readlines()
n = len(raw_text)
numbers = [0]*n
for i in range(n):
    raw_text[i] = raw_text[i].strip()
    numbers[i] = int(raw_text[i])
numbers.sort()
    
#### Find largest number in [1-3] can add

start = 0
jumps = [0, 0, 0]
while(True):
    if start + 1 in numbers:
        start += 1
        jumps[0] += 1
    elif start + 2 in numbers:
        start += 2
        jumps[1] += 1
    elif start + 3 in numbers:
        start += 3
        jumps[2] += 1
    else:
        start += 3
        jumps[2] += 1
        break

#### answer is 1 jumps times 3 jumps
answer = jumps[0] * jumps[2]
print('Answer for Day 10 Part 1 is:', answer)

#### Find number of ways can reach this sum
#### Since always
combinations = [0]*(n)
for i in range(n):
    if numbers[i] <= 3:
        combinations[i] += 1
    for j in range(1,4):
        if numbers[i] + j in numbers:
            ind = numbers.index(numbers[i] + j)
            combinations[ind] += combinations[i]
    
print('Answer for Day 10 Part 2 is:', combinations[n-1])  