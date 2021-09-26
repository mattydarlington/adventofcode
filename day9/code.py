#### Reads data
file = open('data.txt', 'r')
raw_text = file.readlines()
n = len(raw_text)
numbers = [0]*n
for i in range(n):
    raw_text[i] = raw_text[i].strip()
    numbers[i] = int(raw_text[i])
    
#### Check if a number sum of other number
def sum_to_target(numbers, target):
    sort = sorted(numbers)
    n = len(numbers)
    lower = 0
    upper = n-1
    while(lower != upper):
        if sort[lower] + sort[upper] < target:
            lower += 1
        elif sort[lower] + sort[upper] > target:
            upper -= 1
        else:
            return True
    return False

#### Find first term which can't be written as sum of two of the previous
#### 25 numbers in the list
def find_exception(numbers):
    for i in range(25, n):
        if sum_to_target(numbers[i-25:i], numbers[i]) == False:
            return numbers[i]     
        
print('Answer for Day 9 Part 1 is:', find_exception(numbers))  

#### Now need to find consecutive numbers which sum to part one answer
target = find_exception(numbers)            
def find_contiguous(numbers, target):
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += numbers[j]
            if total > target:
                break
            elif total == target:
                return i, j
        
start, stop = find_contiguous(numbers, target)
lower = min(numbers[start: stop+1])
upper = max(numbers[start: stop+1])
answer = lower + upper
print('Answer for Day 9 Part 2 is:', answer)  