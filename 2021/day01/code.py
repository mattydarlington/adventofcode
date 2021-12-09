#### Read Data from txt file
#### and put in list named Data
file = open('data.txt', 'r')
raw_text = file.readlines()
Data = []
n = len(raw_text)
for i in range(n):
    Data.append(int(raw_text[i].strip()))
    
#### Count number of times the depth increases

count = 0
for i in range(1,n):
    if Data[i] > Data[i-1]:
        count += 1
        
print('Answer for Day 1 Part 1 is:', count)

#### Same but with a 3-width sliding window

count = 0
for i in range(1,n-2):
    if sum(Data[i+1:i+4]) > sum(Data[i:i+3]):
        count += 1

print('Answer for Day 1 Part 2 is:', count)   
