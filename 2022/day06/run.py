
from collections import deque

with open('input.txt', 'r') as f:
    line = f.readlines()[0]

def test(l, length):
    fifo = deque(maxlen=length)

    for i, c in enumerate(l):
        fifo.append(c)
        if len(fifo) < length:
            continue

        if len(set(fifo)) == length:
            return i+1

print('Part 1: {}'.format(test(line, 4)))

print('Part 2: {}'.format(test(line, 14)))

