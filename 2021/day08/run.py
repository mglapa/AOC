
import numpy as np
from random import shuffle
import time
from itertools import permutations

#fn = 'sample.txt'
fn = 'input.txt'


def load():
    with open(fn, 'r') as f:
        lines = f.readlines()

    a = []
    b = []
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip().split(' | ')
        a.append(lines[i][0].split(' '))
        b.append(lines[i][1].split(' '))

    return a, b

def part1():
    inp, outp = load()

    total = 0
    for o in outp:
        for d in o:
            if len(d) == 2 or len(d) == 3 or len(d) == 4 or len(d) == 7:
                total += 1

    print('Part 1: ', total)

def display(c):
    prnt = []
    
    # line 0
    l0 = ' ____ ' if c[0] else '      '

    # line 1 + 2
    c0 = '|' if c[1] else ' '
    c1 = '|' if c[2] else ' '
    l1 = '{}    {}'.format(c0, c1)
    l2 = '{}    {}'.format(c0, c1)

    # line 3
    l3 = ' ____ ' if c[3] else '      '

    # line 4
    c0 = '|' if c[4] else ' '
    c1 = '|' if c[5] else ' '
    l4 = '{}    {}'.format(c0, c1)
    l5 = '{}    {}'.format(c0, c1)

    # line 5
    l6 = ' ____ ' if c[6] else '      '

    print()
    for l in [l0, l1, l2, l3, l4, l5, l6]:
        print(l)
    print()

def is_valid(c):
    if c == [1, 1, 1, 0, 1, 1, 1]:
        return True, 0
    if c == [0, 0, 1, 0, 0, 1, 0]:
        return True, 1
    if c == [1, 0, 1, 1, 1, 0, 1]:
        return True, 2
    if c == [1, 0, 1, 1, 0, 1, 1]:
        return True, 3
    if c == [0, 1, 1, 1, 0, 1, 0]:
        return True, 4
    if c == [1, 1, 0, 1, 0, 1, 1]:
        return True, 5
    if c == [1, 1, 0, 1, 1, 1, 1]:
        return True, 6
    if c == [1, 0, 1, 0, 0, 1, 0]:
        return True, 7
    if c == [1, 1, 1, 1, 1, 1, 1]:
        return True, 8
    if c == [1, 1, 1, 1, 0, 1, 1]:
        return True, 9
    return False, None

def part2():
    inp, outp = load()

    '''
    display([1, 1, 1, 0, 1, 1, 1])
    display([0, 0, 1, 0, 0, 1, 0])
    display([1, 0, 1, 1, 1, 0, 1])
    display([1, 0, 1, 1, 0, 1, 1])
    display([0, 1, 1, 1, 0, 1, 0])
    display([1, 1, 0, 1, 0, 1, 1])
    display([1, 1, 0, 1, 1, 1, 1])
    display([1, 0, 1, 0, 0, 1, 0])
    display([1, 1, 1, 1, 1, 1, 1])
    display([1, 1, 1, 1, 0, 1, 1])
    '''

    total = 0
    for idx, (i, o) in enumerate(zip(inp, outp)):
        
        line = i + o
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

        # Iterate through all permutations of the cipher key
        for key in permutations(chars):

            # Iterate through digits in the line
            good = 0
            decoded = ''
            for digit in line:

                # Create 'test' character using the display with the cipher key
                test = [0, 0, 0, 0, 0, 0, 0]
                for c in digit:
                    test[key.index(c)] = 1

                # Check if decoded digit is valid
                # If not, break the loop to move to the next random key
                # If yes, increment 'good' and add the decoded digit to 'decoded'
                valid, char = is_valid(test)
                if valid:
                    good += 1
                    decoded += str(char)
                else:
                    break

            # If all digits in the line were successfully decoded, then break the loop
            if good == len(line):
                break

        # Add get last 4 digits of line (outputs) and add to sum
        total += int(decoded[-4:])

    print('Part 2: ', total)


def main():
    
    part1()

    t0 = time.time()
    part2()
    print('{} s'.format(time.time() - t0))



if __name__ == '__main__':
    main()    























