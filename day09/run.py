
fn = 'input.txt'
N = 25

def parse():
    with open(fn, 'r') as f:
        lines = f.readlines()

    lines = [int(x) for x in lines]
    return lines

# Check if there are any two numbers in code that add up to check
def test(code, check):
    i0 = 0
    i1 = 1
    add = []

    while True:
        try:
            s = code[i0] + code[i1]
        except:
            break
        
        if s == check:
            add.append([i0, i1])

        i1 += 1
        if i1 == N:
            i0 += 1
            i1 = i0 + 1

    return len(add) > 0

# Slide a window of size N through lines and pass into test()
def part1(lines):
    idx0 = 0
    idx1 = N
    while True:
        try:
            code = lines[idx0:idx1]
            check = lines[idx1]
        except:
            break

        valid = test(code, check)
        if valid == False:
            return check

        idx0 += 1
        idx1 += 1

# Slide a window of size "num" through lines and sum all elements in window
def test2(lines, check, num):
    i0 = 0
    i1 = num

    while True:
        if i1 == len(lines):
            return False
        
        s = sum(lines[i0:i1])
        
        if s == check:
            print(min(lines[i0:i1]) + max(lines[i0:i1]))
            return True

        i0 += 1
        i1 += 1

    return False


def part2(lines, check):
    num = 2
    while True:
        try:
            valid = test2(lines, check, num)
            print(valid, num)
            if valid == True:
                break
        except:
            break
        num += 1




lines = parse()

ret = part1(lines)

print('Part 1: ', ret)

part2(lines, ret)



















