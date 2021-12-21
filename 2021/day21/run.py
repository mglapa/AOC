
import numpy as np
from functools import lru_cache

#fn = 'sample.txt'
fn = 'input.txt'

def load():
    with open(fn, 'r') as f:
        lines = f.readlines()

    starts = []
    for l in lines:
        start = int(l.rstrip().split(' ')[-1])-1
        starts.append(start)

    return starts

def part1():
    starts = load()

    scores = [0] * len(starts)

    die = 0
    count = 0

    for j in range(1000):
        for i in range(len(starts)):
            for d in range(3):
                die += 1
                if die == 101:
                    die = 1

                count += 1
                
                starts[i] += die
                starts[i] %= 10
            scores[i] += starts[i] + 1

            if scores[i] >= 1000:
                print('Part 1: ', count*min(scores))
                return

total = 0
wins = [0, 0]

@lru_cache(maxsize=10000000)
def roll(pos1, pos2, score1, score2, roll_val, nroll, pos):
    
    wins1 = 0
    wins2 = 0

    positions = [pos1, pos2]
    scores = [score1, score2]

    positions[pos] += roll_val
    
    if nroll == 3:

        positions[pos] %= 10
        scores[pos] += positions[pos]+1

        if scores[pos] >= 21:
            return (1, 0) if pos==0 else (0, 1)

        nroll = 0
        pos += 1
        if pos == len(positions):
            pos = 0
    
    for i in range(1, 4):
        a, b = roll(positions[0], positions[1], scores[0], scores[1], i, nroll+1, pos)
        wins1 += a
        wins2 += b

    return wins1, wins2
    


def part2():
    positions = load()

    wins1 = 0
    wins2 = 0

    for i in range(1, 4):
        a, b = roll(positions[0], positions[1], 0, 0, i, nroll=1, pos=0)
        wins1 += a
        wins2 += b

    print('Part 2: ', max(wins1, wins2))

def main():
    
    part1()

    part2()


if __name__ == '__main__':
    main()    























