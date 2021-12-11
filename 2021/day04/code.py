import numpy as np

#### Read Data from txt file
#### and put in list named Data
file = open('data.txt', 'r')
raw_text = file.readlines()

numbers = raw_text[0].split(',')
n_numbers = len(numbers)
for i in range(n_numbers):
    numbers[i] = int(numbers[i])

n_boards = int((len(raw_text) - 1)/6)
boards = np.zeros((n_boards,5,5), int)
for i in range(n_boards):
    board = [[0]*5]*5
    for j in range(5):
        board[j] = raw_text[6*i + j + 2].split()
    for j in range(5):
        for k in range(5):
            board[j][k] = int(board[j][k])
    boards[i] = np.array(board)
    
def check_win(board, numbers):
    for i in range(5):
        if set(board[i,:]) <= set(numbers) or set(board[:,i]) <= set(numbers):
            return 1
    return 0

def find_winner(boards, numbers):
    n_numbers = len(numbers)
    for i in range(n_numbers):
        for board in boards:
            if check_win(board, numbers[:i]):
                return board, numbers[i-1], i
    return 0

def give_answer(boards, numbers):
    board, last, i = find_winner(boards, numbers)
    uncalled = set(board.flatten()) - set(numbers[:i])
    return sum(uncalled) * last

print('Answer for Day 4 Part 1 is:', give_answer(boards, numbers))

def find_loser(boards, numbers):
    n_numbers = len(numbers)
    i = 0
    while(len(boards) > 1):
        j = 0
        while(j < len(boards)):
            if check_win(boards[j], numbers[:i]):
                boards = np.delete(boards, j, 0)
            else:
                j += 1
        i += 1
    while(not check_win(boards[0], numbers[:i])):
        i += 1
    return boards, numbers[i-1], i

def give_answer(boards, numbers):
    board, last, i = find_loser(boards, numbers)
    uncalled = set(board.flatten()) - set(numbers[:i])
    return sum(uncalled) * last

print('Answer for Day 4 Part 2 is:', give_answer(boards, numbers))   
