

def parse():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    lines = [int(x) for x in lines]
    lines.append(0)
    lines = sorted(lines)
    lines.append(lines[-1]+3)
    return lines


def part1(lines):
    ones = 0
    threes = 0

    for i in range(1, len(lines)):
        diff = lines[i] - lines[i-1]
        
        if diff == 1:
            ones += 1
        if diff == 3:
            threes += 1

    print('Part 1: ', ones*threes)

class node:
    def __init__(self, val):
        self.val = val
        self.next = []

# Get a list of the next adapters that the current one can connect to
def get_next(lines, idx):
    ret = []
    leaves = 0

    val = lines[idx]

    start = idx+1
    end = min(idx+4, len(lines))
    for i in range(start, end):
        if (lines[i] - val) <= 3:
            ret.append(i)

            # Check if it's the last node
            if i == len(lines) - 1:
                leaves += 1
    return leaves, ret


def step(lines, idx):
    new = node(idx)
    leaves, new.next = get_next(lines, idx)
    
    for n in new.next:
        if n in known.keys():
            leaves += known[n]
        else:
            leaves += step(lines, n)

    return leaves

known = {}

def part2(lines):
    for idx in range(len(lines)-1, -1, -1):
        print(idx)
        leaves = step(lines, idx)
        known[idx] = leaves
    
    print('Part 2: ', known[0])









lines = parse()

part1(lines)

part2(lines)


