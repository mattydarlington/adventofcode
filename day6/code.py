#### Reads data and creates list of unique answers
#### Need to seperate data by empty lines to get passports
file = open('data.txt', 'r')
raw_text = file.readlines()
n = len(raw_text)
answers_nonunique = ['']
for i in range(n):
    raw_text[i] = raw_text[i].strip()
            
m = 0
for i in range(n):
    if raw_text[i] == '':
        answers_nonunique.append('')
        m += 1
    else:
        answers_nonunique[m] += raw_text[i] 
m += 1
        
answers = []
for i in range(m):
    answers.append(list(set(answers_nonunique[i])))
    
#### Part 1 just needs to sum over these to get total unique answers for all groups

total = 0
for i in range(m):
    total += len(answers[i])
print('Answer for Day 6 Part 1 is:', total)    

#### Everyone in group now needs to say yes
#### First find group sizes

group_size = [0]*m
m = 0
for i in range(n):
    if raw_text[i] == '':
        m += 1
    else:
        group_size[m] += 1
m += 1

#### Check if everyone says yes
total = 0
for i in range(m):
    for char1 in answers[i]:
        subtotal = 0
        for char2 in answers_nonunique[i]:
            if char1 == char2:
                subtotal += 1
        if subtotal == group_size[i]:
            total += 1
print('Answer for Day 6 Part 2 is:', total)        
        