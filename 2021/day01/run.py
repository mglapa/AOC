
def load():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = int(lines[i])

    return lines

def part1(lines):
    count = 0
    for i in range(len(lines)-1):
        if lines[i+1] > lines[i]:
            count += 1
    print('Part 1: ', count)

def part2(lines):
    sums = []
    for i in range(len(lines)-2):
        tmp = lines[i] + lines[i+1] + lines[i+2]
        sums.append(tmp)

    count = 0
    for i in range(len(sums)-1):
        if sums[i+1] > sums[i]:
            count += 1
    print('Part 2: ', count)

def main():    
    
    lines = load()

    part1(lines)

    part2(lines)

if __name__ == '__main__':
    main()





















