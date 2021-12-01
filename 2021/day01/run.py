
def load():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = int(lines[i])

    return lines

def part1():
    count = 0
    for i in range(len(lines)-1):
        if lines[i+1] > lines[i]:
            count += 1
    print(count)

def part2():
    sums = []
    for i in range(len(lines)-2):
        tmp = lines[i] + lines[i+1] + lines[i+2]
        sums.append(tmp)

    count = 0
    for i in range(len(sums)-1):
        if sums[i+1] > sums[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    
    lines = load()

    part1()

    part2()
























