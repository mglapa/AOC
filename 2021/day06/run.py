
import numpy as np
import time

def load():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return np.array(lines[0].rstrip().split(','), dtype=np.int)

# The stupid way
def part1_bruteforce():
    t_start = time.time()
    data = load()
    for i in range(80):
        t0 = time.time()
        data -= 1

        new = len(data[data<0])
        data[data<0] = 6

        for j in range(new):
            data = np.append(data, 8)

        t1 = time.time()

        if i >= 60:
            print('Day: {:d}  |  Time: {:.2f} s'.format(i, t1 - t0))

    print('Part 1: ', len(data))
    print('Time: {:.1f} s'.format(time.time() - t_start))

def run(data, n):
    counts = np.zeros(9, dtype=np.int)

    for i in range(0, 9):
        counts[i] = len(data[data==i])

    for i in range(n):
        breed = counts[0]
        counts = np.delete(counts, 0)
        counts[6] += breed
        counts = np.append(counts, breed)

    return sum(counts)

def part1():
    data = load()
    total = run(data, 80)
    print('Part 1: ', total)

def part2():
    data = load()
    total = run(data, 256)
    print('Part 2: ', total)

def main():
    
    #part1_bruteforce()

    part1()
    
    part2()


if __name__ == '__main__':
    main()    























