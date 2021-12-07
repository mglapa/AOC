
import numpy as np
import time

#fn = 'sample.txt'
fn = 'input.txt'

def load():
    with open(fn, 'r') as f:
        lines = f.readlines()
    pos = lines[0].split(',')
    pos = np.array(pos, dtype=np.int)
    return pos

solved = {}
def check_fuel(pos, x):
    total = 0
    deltas = abs(pos - x)

    for d in deltas:
        tmp = 0
        keys = solved.keys()
        for i in range(d, 0, -1):
            if i in keys:
                tmp += solved[i]
                break
            else:
                tmp += i
        total += tmp
        if d not in keys:
            solved[d] = tmp
    return total 

def part1():
    pos = load()
    
    best_fuel = 1e20
    best_idx = -1
    for i in range(pos.min(), pos.max()):
        fuel = sum(abs(pos - i))
        if fuel < best_fuel:
            best_fuel = fuel
            best_idx = i

    print('Part 1: {}'.format(best_fuel))

def part2():
    pos = load()

    best_fuel = 1e20
    best_idx = -1
    for i in range(pos.min(), pos.max()):
        fuel = check_fuel(pos, i)

        if fuel < best_fuel:
            best_fuel = fuel
            best_idx = i

    print('Part 2: {}'.format(best_fuel))

def main():
    
    part1()

    part2()

if __name__ == '__main__':
    main()    























