
import numpy as np

def load():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = [int(a) for a in lines[i].rstrip()]
    return lines

def part1(lines):
    data = np.array(lines)
    dim = data.shape
    gamma = ''
    eps = ''

    for i in range(dim[1]):
        col = data[:, i]
        col = str(col)
        zeros = col.count('0')
        ones = col.count('1')

        if ones > zeros:
            gamma += '1'
            eps += '0'
        elif zeros > ones:
            gamma += '0'
            eps += '1'
        else:
            print('o no')
            exit()

    gamma = int(gamma, base=2)
    eps = int(eps, base=2)

    print('Part 1: ', gamma*eps)

def part2(lines):
    orig = np.array(lines)

    data = orig.copy()
    for i in range(data.shape[1]):
        filtered = []
        
        col = data[:, i]
        col = str(col)
        zeros = col.count('0')
        ones = col.count('1')

        if ones >= zeros:
            key = 1 
        else:
            key = 0

        for j in range(data.shape[0]):
            if data[j, i] == key:
                filtered.append(data[j])

        data = np.array(filtered)
    
    a = ''
    for c in data[0]:
        a += str(c)

    oxygen = int(a, base=2)

    data = orig.copy()
    for i in range(data.shape[1]):
        filtered = []
        
        col = data[:, i]
        col = str(col)
        zeros = col.count('0')
        ones = col.count('1')

        if ones >= zeros:
            key = 0 
        else:
            key = 1

        for j in range(data.shape[0]):
            if data[j, i] == key:
                filtered.append(data[j])

        data = np.array(filtered)
        if data.shape[0] == 1:
            break
    
    a = ''
    for c in data[0]:
        a += str(c)

    co2 = int(a, base=2)

    print('Part 2: ', oxygen*co2)

def main():
    
    lines = load()

    part1(lines)

    part2(lines)

if __name__ == '__main__':
    main()    























