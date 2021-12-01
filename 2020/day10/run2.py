

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

# Get a list of the next adapters that the current one can connect to
def get_next(lines, idx):
    ret = []
    leaves = 0
    val = lines[idx] # Value at current node

    # Iterate through the next 3 adapters to see if any are compatible
    start = idx+1
    end = min(idx+4, len(lines))
    for i in range(start, end):
        if (lines[i] - val) <= 3:
            ret.append(i)

            # Check if it's the last node
            if i == len(lines) - 1:
                leaves += 1

    return leaves, ret

# Recursive function: find all paths from idx
def step(lines, idx):
    
    # Find direct connections from idx
    leaves, nxt = get_next(lines, idx)
    
    # Iterate through child nodes and find all paths from each one to the end
    for n in nxt:
        if n in known.keys():
            leaves += known[n]
        else:
            leaves += step(lines, n)

    return leaves

known = {}

def part2(lines):
    # Iterate BACKWARDS
    for idx in range(len(lines)-1, -1, -1):
        leaves = step(lines, idx)
        known[idx] = leaves
    
    print('Part 2: ', known[0])

# Main
lines = parse()
for l in lines:
    print(l)

part1(lines)

part2(lines)


