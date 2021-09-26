#### Reads data and creates passports
#### Need to seperate data by empty lines to get passports

file = open('data.txt', 'r')
raw_text = file.readlines()
n = len(raw_text)
passport = ['']
for i in range(n):
    raw_text[i] = raw_text[i].strip()
            
m = 0
for i in range(n):
    if raw_text[i] == '':
        passport.append('')
        m += 1
    else:
        passport[m] += raw_text[i] + ' '
    
#### Check passports
#### Fine if 'cid' missing 
#### Need all other
#### byr (Birth Year)
#### iyr (Issue Year)
#### eyr (Expiration Year)
#### hgt (Height)
#### hcl (Hair Color)
#### ecl (Eye Color)
#### pid (Passport ID)
#### cid (Country ID)

def check_passport(passport):
    split_passport = passport.split()
    n = len(split_passport)
    fields = []
    for i in range(n):
        fields.append(split_passport[i][0:3])
    unique_fields = list(set(fields))
    if len(unique_fields) == 8:
        return True
    if len(unique_fields) == 7:
        for i in range(7):
            if unique_fields[i] == 'cid':
                return False
        return True
    return False

answer = 0
for i in range(m):
    answer += check_passport(passport[i])
print('Answer for Day 4 Part 1 is:', answer)

#### Now need to improve passport check to follow these rules
#### byr (Birth Year) - four digits; at least 1920 and at most 2002.
#### cid (Country ID) - ignored, missing or not.
#### ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#### eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#### hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#### hgt (Height) - a number followed by either cm or in:
#### If cm, the number must be at least 150 and at most 193.
#### If in, the number must be at least 59 and at most 76.
#### iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#### pid (Passport ID) - a nine-digit number, including leading zeroes.

def check_passport(passport):
    split_passport = sorted(passport.split())
    fields = []
    values = []
    #### Remove CID
    if split_passport[1][0:3] == 'cid':
        split_passport.pop(1)
    
    #### Split into fields and values
    n = len(split_passport)
    for i in range(n):
        split = split_passport[i].split(':')
        fields.append(split[0])
        values.append(split[1])
    boolean = [0] * 7
    
    #### Check all fields present
    fields_sorted = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    if fields != fields_sorted:
        return False
    #### Check all values correct
    if 1920 <= int(values[0]) <= 2002:
        boolean[0] = 1
        
    eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if values[1] in eye_color:
        boolean[1] = 1
    
    if 2020 <= int(values[2]) <= 2030:
        boolean[2] = 1
    
    boolean[3] = 1
    for char in values[3][1:]:
        if char not in "0123456789abcdef":
            boolean[3] = 0
    if len(values[3]) != 7:
        boolean[3] = 0
        
    if values[4][-2:] == 'cm':
        if 150 <= int(values[4][:-2]) <= 193:
            boolean[4] = 1
    elif values[4][-2:] == 'in':
        if  59 <= int(values[4][:-2]) <= 76:
            boolean[4] = 1
               
    if 2010 <= int(values[5]) <= 2020:
        boolean[5] = 1
    
    boolean[6] = 1
    for char in values[6]:
        if char not in "0123456789":
            boolean[6] = 0
    if len(values[6]) != 9:
        boolean[6] = 0
        
    if sum(boolean) == 7:
        return True
    else:
        return False
    
answer = 0
for i in range(m):
    answer += check_passport(passport[i])
print('Answer for Day 4 Part 2 is:', answer)