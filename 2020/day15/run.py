
def parse():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    line = lines[0].rstrip().split(',')
    for i in range(len(line)):
        line[i] = int(line[i])
    return line

def part1(line, N):
    while True:
        if len(line) == N:
            break

        val = line[-1]
        if val in line[:-1]:
            line.reverse()
            idx = line[1:].index(val)
            idx = len(line) - idx - 2
            line.reverse()
            #print(len(line)-1, idx)
            line.append(len(line) - 1 - idx)
        else:
            line.append(0)
        #print(line)
    print('Part 1: ', line[-1])

def part2(line, N):
    indices = {}
    count = 1
    for l in line[:-1]:
        indices[l] = count
        count += 1

    prev = line[-1]
    while True:
        if count % 1000000 == 0:
            print('{:2.2f}'.format(count * 100 / N))

        if prev in indices.keys():
            idx = indices[prev]
            val = count - idx
            indices[prev] = count
            prev = val
        else:
            indices[prev] = count
            prev = 0

        count += 1
        if count == N:
            print('Part 2: ', prev)
            break
    
line = parse()
part1(line.copy(), 2020)

# Part 2
part2(line.copy(), 30000000)







