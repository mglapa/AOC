
# transform initial condition so that each stack/column is in a list
def init(crates):
    cols = []
    for x in range(1, len(crates[0]), 4):
        stack = []
        for y in range(len(crates)-1, -1, -1):
            c = crates[y][x]
            if c != ' ':
                stack.append(c)
        cols.append(stack)
    return cols

# Read input
with open('input.txt', 'r') as f:
    lines = f.read()

# Split lines into initial condition and list of moves
crates, moves = lines.split('\n\n')
crates = crates.split('\n')[:-1]
moves = moves.strip().split('\n')

# Parse list of moves
for i in range(len(moves)):
    moves[i] = moves[i].split(' ')
    moves[i] = [int(moves[i][1]), int(moves[i][3]), int(moves[i][5])]

# Get initial condition
cols = init(crates)

# Process moves
for m in moves:
    for i in range(m[0]):
        cols[m[2]-1].append(cols[m[1]-1].pop(-1))

# Get top crate from each column and print
ans1 = ''.join([c[-1] for c in cols])
print('Part 1: {}'.format(ans1))

# Get initial condition
cols = init(crates)

# Process moves
for m in moves:
    tmp = []
    for i in range(m[0]):
        tmp.append(cols[m[1]-1].pop(-1))
    
    tmp.reverse()
    for t in tmp:
        cols[m[2]-1].append(t)

# Get top crate from each column and print
ans2 = ''.join([c[-1] for c in cols])
print('Part 2: {}'.format(ans2))


