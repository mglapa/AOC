
def parse():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    return lines

def store1(val, mask):
    mask_and = int(mask.replace('X', '1'), 2)
    mask_or = int(mask.replace('X', '0'), 2)
    mask_36 = (2**36) - 1
    return ((val & mask_and) | mask_or) & mask_36

def part1(lines):
    mem = {}
    for l in lines:
        if 'mask' in l:
            mask = l.split()[-1]
        if 'mem' in l:
            idx = int(l.split()[0].replace('mem[', '').replace(']', ''))
            val = int(l.split()[-1])
            mem[idx] = store1(val, mask)

    total = 0
    for key in mem.keys():
        total += mem[key]

    print('Part 1: ', total)

def store2(val, addr, mem, mask):
    # Pad addr to 36 bits with leading zeros
    addr = '{:036b}'.format(addr)
    
    # Mask addr
    new_addr = ''
    for i in range(36):
        b = mask[i]
        if b == '1':
            new_addr += b
        elif b == 'X':
            new_addr += '{}'
        elif b == '0':
            new_addr += addr[i]

    count = mask.count('X')
    for i in range(2**count):
        sub = '{:036b}'.format(i)[-count:]
        addr = new_addr.format(*[x for x in sub])
        mem[addr] = val

def part2(lines):
    mem = {}
    for l in lines:
        if 'mask' in l:
            mask = l.split()[-1]
        if 'mem' in l:
            addr = int(l.split()[0].replace('mem[', '').replace(']', ''))
            val = int(l.split()[-1])
            store2(val, addr, mem, mask)

    total = 0
    for key in mem.keys():
        total += mem[key]

    print('Part 2: ', total)

lines = parse()

part1(lines)

part2(lines)


