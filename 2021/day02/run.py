
def load():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    return lines

def part1(lines):
    h = 0
    d = 0

    for line in lines:
        cmd, val = line.rstrip().split(' ')
        val = int(val)

        if cmd == 'forward':
            h += val
        if cmd == 'down':
            d += val
        if cmd == 'up':
            d -= val

    print('Part 1: ', d*h)

def part2(lines):
    h = 0
    d = 0
    aim = 0

    for line in lines:
        cmd, val = line.rstrip().split(' ')
        val = int(val)

        if cmd == 'forward':
            h += val
            d += aim*val
        if cmd == 'down':
            aim += val
        if cmd == 'up':
            aim -= val

    print('Part 2: ', d*h)

def main():
    
    lines = load()

    part1(lines)

    part2(lines)


if __name__ == '__main__':
    main()    























