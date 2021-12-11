
import numpy as np

#fn = 'sample.txt'
fn = 'input.txt'

def load():
    with open(fn, 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = list(lines[i].rstrip())

    lines = np.array(lines, dtype=np.int)

    return lines

def part1():
    lines = load()

    count, _ = find_low_pts(lines)
    print('Part 1: ', count)

def find_low_pts(lines):
    h, w = lines.shape
    count = 0
    low_pts = []
    for x in range(w):
        for y in range(h):
            val = lines[y, x]
            try:
                x0 = lines[y, x-1]
            except:
                x0 = 1e10

            try:
                x1 = lines[y, x+1]
            except:
                x1 = 1e10

            try:
                y0 = lines[y-1, x]
            except:
                y0 = 1e10

            try:
                y1 = lines[y+1, x]
            except:
                y1 = 1e10
            
            if val < x0 and val < x1 and val < y0 and val < y1:
                count += (1+val)
                low_pts.append([x, y])

    return count, low_pts

def check_neighbors(lines, x, y, marked):
    count = 0
    low_neighbors = []
    
    try:
        idx = [x-1, y]
        if idx not in marked and idx[0] >=0 and idx[1] >= 0:
            test = lines[idx[1], idx[0]]
            if test < 9:
                count += 1
                low_neighbors.append(idx)
                marked.append(idx)
    except:
        pass

    try:
        idx = [x+1, y]
        if idx not in marked and idx[0] >=0 and idx[1] >= 0:
            test = lines[idx[1], idx[0]]
            if test < 9:
                count += 1
                low_neighbors.append(idx)
                marked.append(idx)
    except:
        pass

    try:
        idx = [x, y-1]
        if idx not in marked and idx[0] >=0 and idx[1] >= 0:
            test = lines[idx[1], idx[0]]
            if test < 9:
                count += 1
                low_neighbors.append(idx)
                marked.append(idx)
    except:
        pass

    try:
        idx = [x, y+1]
        if idx not in marked and idx[0] >=0 and idx[1] >= 0:
            test = lines[idx[1], idx[0]]
            if test < 9:
                count += 1
                low_neighbors.append(idx)
                marked.append(idx)
    except:
        pass

    for p in low_neighbors:
        x, y = p
        count += check_neighbors(lines, x, y, marked)

    return count


def part2():
    lines = load()
    
    _, pts = find_low_pts(lines)
    sizes = []

    marked = pts.copy()

    for p in pts:
        x, y = p
        num = 1 + check_neighbors(lines, x, y, marked)
        sizes.append(num)

    sizes = sorted(sizes, reverse=True)

    print('Part 2: ', sizes[0]*sizes[1]*sizes[2])

def main():
    
    part1()

    part2()


if __name__ == '__main__':
    main()    























