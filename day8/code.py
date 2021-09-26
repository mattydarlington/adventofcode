#### Reads data
file = open('data.txt', 'r')
raw_text = file.readlines()
n = len(raw_text)
answers_nonunique = ['']
for i in range(n):
    raw_text[i] = raw_text[i].strip()
    
#### acc changes variable    
#### jmp moves instruction
#### nop does nothing
def run_code(instruction):
    path = []
    acc = 0
    i = 0
    while True:
        for j in path:
            if j == i:
                return acc
        path.append(i)
        if instruction[i][0:3] == 'acc':
            acc += int(instruction[i][4:])
            i += 1
        elif instruction[i][0:3] == 'jmp':
            i += int(instruction[i][4:])
        else:
            i += 1
    
print('Answer for Day 8 Part 1 is:', run_code(raw_text))  

#### Need to change a nop to jmp or vica versa so code runs

def try_code(instruction):
    path = []
    acc = 0
    i = 0
    while True:
        if i == n:
            return acc
        for j in path:
            if j == i:
                return 'Inf'
        path.append(i)
        if instruction[i][0:3] == 'acc':
            acc += int(instruction[i][4:])
            i += 1
        elif instruction[i][0:3] == 'jmp':
            i += int(instruction[i][4:])
        else:
            i += 1
            
def fix_code(text):
    for i in range(n):
        text_try = text.copy()
        if text[i][0:3] == 'jmp':
            text_try[i] = text_try[i].replace('jmp', 'nop')
        if text[i][0:3] == 'nop':
            text_try[i] = text_try[i].replace('nop', 'jmp')
        if try_code(text_try) != 'Inf':
            return try_code(text_try)
            
print('Answer for Day 8 Part 2 is:', fix_code(raw_text))  