#### Reads data
file = open('data.txt', 'r')
raw_text = file.readlines()
n = len(raw_text)
answers_nonunique = ['']
for i in range(n):
    raw_text[i] = raw_text[i].strip()
    
outer = []
inner = []   
for i in range(n):
    string = raw_text[i].split(' bags contain ')
    outer.append(string[0])
    bags = []
    if string[1] != 'no other bags.':
        right_string = string[1].split(', ')
        for j in range(len(right_string)):
            mix = right_string[j].split(' bag')
            trash = ['', 's', 's.', '.']
            for bag in mix:
                if bag not in trash:
                    bags.append(bag)
    inner.append(bags)
                    
#### Need to find bags which can eventually hold a shiny gold
#### First find which directly hold shiny gold
shiny_gold = [0]*n
for i in range(n):
    bags = inner[i]
    for bag in bags:
        if bag[2:] == 'shiny gold':
            shiny_gold[i] = 1
#### Create a boolean vector if can hold shiny gold
#### Keep checking if a bag can hold a bag which can hold shiny gold
for _ in range(n-1):
    for i in range(n):
        bags = inner[i]
        no_bag = len(bags)
        for j in range(no_bag):
            ind = outer.index(bags[j][2:])
            if shiny_gold[ind] == 1:
                shiny_gold[i] = 1


print('Answer for Day 7 Part 1 is:', sum(shiny_gold))  

#### Now need to find how many bags a shiny gold bag must contain
#### Calculate recursively
def bags_inside(colour, inner):
    col_ind = outer.index(colour)
    col_inner = inner[col_ind]
    if len(col_inner) == 0:
        return 0
    else:
        no = []
        col = []
        for bag in col_inner:
            col.append(bag[2:])
            no.append(bag[:1])
        total = 0
        for i in range(len(no)):
            total += int(no[i]) * (bags_inside(col[i], inner) + 1)
    return total
    
print('Answer for Day 7 Part 2 is:', bags_inside('shiny gold', inner))  