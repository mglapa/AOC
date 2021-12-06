
import numpy as np

def load():
    with open('input.txt', 'r') as f:
        lines = f.read()

    draws = lines.split('\n').pop(0).rstrip().split(',')

    boards = lines.split('\n\n')
    boards.pop(0)

    for i in range(len(boards)):
        boards[i] = boards[i].rstrip().split('\n')
        for j in range(len(boards[i])):
            boards[i][j] = [int(s) for s in boards[i][j].split() if s.isdigit()]

    boards = np.array(boards)
    marks = np.zeros_like(boards)

    return draws, boards, marks

def check_winner(board):
    for i in range(5):
        if sum(board[i, :]) == 5:
            return True
        if sum(board[:, i]) == 5:
            return True
        #if sum(board.diagonal()) == 5:
        #    return True
        #if sum(np.fliplr(board).diagonal()) == 5:
        #    return True
    return False

def part1():

    draws, boards, marks = load()

    # Iterate through draws and and place marks
    for num in draws:
        idx = boards==int(num)
        marks[idx] = 1

        # Iterate through boards and check for winners
        winner = -1
        for i, m in enumerate(marks):
            if check_winner(m):
                winner = i
        if winner >= 0:
            break

    boards[winner][marks[winner]==1] = 0

    print('Part 1: {}'.format(boards[winner].sum() * int(num)))

def part2():

    draws, boards, marks = load()

    winners = []

    # Iterate through draws and and place marks
    for num in draws:
        
        idx = boards==int(num)
        marks[idx] = 1

        # Iterate through boards and check for winners
        for i, m in enumerate(marks):
            if check_winner(m):
                if i not in winners:
                    last = num
                    winners.append(i)
        
        if len(winners) == len(boards):
            break

    idx = winners[-1]
    boards[idx][marks[idx]==1] = 0
    print('Part 2: {}'.format(boards[idx].sum() * int(last)))


def main():
    
    part1()

    part2()


if __name__ == '__main__':
    main()    























