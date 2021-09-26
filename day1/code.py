#### Read Data from txt file
#### and put in list named Data
file = open('data.txt', 'r')
raw_text = file.readlines()
Data = []
n = len(raw_text)
for i in range(n):
    Data.append(int(raw_text[i].strip()))
    
#### Find two integers which sum to 2020
#### Sort data
Data = sorted(Data)

def two_sum(Data, target):
    n = len(Data)
    lower = 0
    upper = n-1
    
    while(True):
        if lower == upper:
            break
        elif Data[lower] + Data[upper] < 2020:
            lower += 1
        elif Data[lower] + Data[upper] > 2020:
            upper -= 1
        else:
            return lower, upper
    
lower, upper = two_sum(Data, 2020)
answer = Data[lower] * Data[upper]
print('Answer for Day 1 Part 1 is:', answer)


#### Find three integers which sum to 2020
def three_sum(Data, target):
    n = len(Data)
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if Data[i]+Data[j]+Data[k] == 2020:
                    return i, j, k
            
i, j, k = three_sum(Data, 2020)
answer = Data[i]*Data[j]*Data[k]
print('Answer for Day 1 Part 2 is:', answer)