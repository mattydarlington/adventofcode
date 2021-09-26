#### re package for string splitting
import re

#### Read Data from txt file
#### Put in 4 lists
#### Lower, Upper, Character and Password
file = open('data.txt', 'r')
raw_text = file.readlines()
lower, upper, character, password = [], [], [], []
n = len(raw_text)
for i in range(n):
    raw_text[i] = raw_text[i].strip()
    split = re.split('-|: | ', raw_text[i])
    lower.append(int(split[0]))
    upper.append(int(split[1]))
    character.append(split[2])
    password.append(split[3])
    
#### Check if a password has between the upper and lower of the given character
def password_check(lower, upper, character, password):
    n = len(password)
    count = 0
    for i in range(n):
        if password[i] == character:
            count += 1
    if count >= lower and count <= upper:
        return True
    else:
        return False
    
#### Check how many passwords meet criteria
answer = 0
for i in range(n):
    answer += password_check(lower[i], upper[i], character[i], password[i])
    
print('Answer for Day 2 Part 1 is:', answer)
    
#### Need different password check
#### Either lower or upper must be character - not both !!

def password_check(lower, upper, character, password):
    n = len(password)
    char1 = False
    char2 = False
    if lower - 1 < n:
        if password[lower - 1] == character:
            char1 = True
    if upper - 1 < n:
        if password[upper - 1] == character:
            char2 = True
    return char1^char2
    
#### Check how many passwords meet criteria
answer = 0
for i in range(n):
    answer += password_check(lower[i], upper[i], character[i], password[i])
    
print('Answer for Day 2 Part 2 is:', answer)
    