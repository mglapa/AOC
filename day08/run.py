
def part1(lines):
    accumulator = 0
    counter = 0
    ran = []
    
    # Iterate through program lines
    while True:
        try:
            cmd, val = lines[counter].split(' ')
            val = int(val)
        except:
            break
        
        # Check if a line has already run
        if counter in ran:
            break
        else:
            ran.append(counter)

        # Perform the op
        if cmd == 'nop':
            counter += 1
            continue
        if cmd == 'acc':
            accumulator += val
            counter += 1
            continue
        if cmd == 'jmp':
            counter += val

    print('Part 1: ', accumulator)

# Function to run a test - replace the command at a given line, then run code, check for loops
def test(lines, switch):
    accumulator = 0
    counter = 0
    ran = []

    # Check op at line 'switch' - replace nop with jmp and vice versa
    if 'jmp' in lines[switch]:
        lines[switch] = lines[switch].replace('jmp', 'nop')
    else:
        lines[switch] = lines[switch].replace('nop', 'jmp')

    # Iterate through program lines
    while True:
        try:
            cmd, val = lines[counter].split(' ')
            val = int(val)
        except:
            print('counter is at {} out of {} instructions'.format(counter, len(lines)))
            print('Changed op is on line {}'.format(switch))
            print('Accumulator: {}'.format(accumulator))
            return True
        
        # Check if a line has already run
        if counter in ran:
            return False
        else:
            ran.append(counter)

        # Perform the op
        if cmd == 'nop':
            counter += 1
            continue
        if cmd == 'acc':
            accumulator += val
            counter += 1
            continue
        if cmd == 'jmp':
            counter += val

def part2(lines):
    mod = []
    
    for i in range(len(lines)):
        if 'nop' in lines[i] or 'jmp' in lines[i]:
            mod.append(i)

    for l in mod:
        ret = test(lines.copy(), l)
        if ret == True:
            break

# Main
with open('input.txt', 'r') as f:
    orig_lines = f.readlines()

part1(orig_lines)

part2(orig_lines)















