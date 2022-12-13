
with open('input.txt', 'r') as f:
    lines = f.readlines()

X = 1
i = 1
sig = 0

screen = []
line = []

# The sprite starts at 0,1,2, so the first line always starts with #
line.append('#')

def helper():
    global i
    global line
    global sig

    i += 1
    
    pos = (i-1)%40
    if pos == X or pos == (X-1) or pos == (X+1):
        line.append('#')
    else:
        line.append('.')
        
    if (i-0)%40==0:
        screen.append(line)
        line = []
    
    if (i+20)%40 == 0:
        sig += i*X

# Iterate through instructions
for l in lines:
    cmd = l.strip().split(' ')

    if cmd[0] == 'noop':
        helper()

    elif cmd[0] == 'addx':
        # addx instruction takes two cycles, but we need to check
        # cycle count after both cycles
        for j in range(2):
            if j == 1:
                X += int(cmd[1])
            helper()

print('Part 1: {}'.format(sig))

print('Part 2:')
for s in screen:
    print(''.join(s))

