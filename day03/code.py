#### Reads data and creates slope list

file = open('data.txt', 'r')
raw_text = file.readlines()
n = len(raw_text)
slope = []
for i in range(n):
    raw_text[i] = raw_text[i].strip()
    slope.append(raw_text[i])

#### Find how many trees encountered
#### Make moves defined by a number down and number right

def trees_encountered(slope, right, down):
    height = len(slope)
    width = len(slope[0])
    position = [height-1,0]
    trees = 0
    while (position[0] >= 0):
        if slope[(n-1)-position[0]][position[1]] == '#':
            trees += 1
        position[0] -= down
        position[1] += right
        if position[1] >= width:
            position[1] = position[1]%width
    return trees
            
answer = trees_encountered(slope, 3, 1)
print('Answer for Day 3 Part 1 is:', answer)

#### Now traverse the slope five different ways
#### Right 1, down 1.
#### Right 3, down 1. (This is the slope you already checked.)
#### Right 5, down 1.
#### Right 7, down 1.
#### Right 1, down 2.

answer = trees_encountered(slope,1,1)
answer *= trees_encountered(slope,3,1)
answer *= trees_encountered(slope,5,1)
answer *= trees_encountered(slope,7,1)
answer *= trees_encountered(slope,1,2)
print('Answer for Day 3 Part 2 is:', answer)