#### Read Data from txt file
#### and put in list named Data
file = open('data.txt', 'r')
raw_text = file.readlines()
n = len(raw_text)
Data = []
for i in range(n):
    Data.append(raw_text[i].split()[0])

### Most and Least common bits

gamma = ""
epsilon = ""
m = len(Data[0])
for i in range(m):
    count = 0
    for j in range(n):
        count += int(Data[j][i])
    gamma += str(round(count/n))
    epsilon += str(1 - round(count/n))

print('Answer for Day 3 Part 1 is:', int(gamma,2) * int(epsilon, 2))

### Discard the least and most common bits

j = 0
remaining = Data.copy()
while(len(remaining) > 1):
    i = 0
    count = 0
    for k in range(len(remaining)):
        count += int(remaining[k][j])
    common = str(round(count/len(remaining) + 1/(2*n)))
    while(i < len(remaining)):
        if remaining[i][j] != common:
            remaining.pop(i)
        else:
            i += 1
    j += 1
    
oxygen = remaining[0]

j = 0
remaining = Data.copy()
while(len(remaining) > 1):
    i = 0
    count = 0
    for k in range(len(remaining)):
        count += int(remaining[k][j])
    least = str(1-round(count/len(remaining) + 1/(2*n)))
    while(i < len(remaining)):
        if remaining[i][j] != least:
            remaining.pop(i)
        else:
            i += 1
    j += 1
    
co2 = remaining[0]


print('Answer for Day 3 Part 2 is:', int(oxygen,2) * int(co2,2))   

