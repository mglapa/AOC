
import numpy as np

def parse():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = [x for x in lines[i].rstrip()]

    lines = np.array(lines)

    return lines


def change1(seatmap):
    seatmap_new = seatmap.copy()
    
    y_dim, x_dim = seatmap.shape
    for y in range(y_dim):
        for x in range(x_dim):
            #print(seatmap[y, x], end='')
            
            if seatmap[y, x] == 'L':

                x0 = max(0, x-1)
                x1 = min(x_dim, x+1)
                y0 = max(0, y-1)
                y1 = min(y_dim, y+1)

                window = seatmap[y0:y1+1, x0:x1+1]
                empty = np.count_nonzero(window=='L') - 1 # Subtract current seat
                filled = np.count_nonzero(window=='#')
                floor = np.count_nonzero(window=='.')

                if filled == 0:
                    seatmap_new[y, x] = '#'
            
            if seatmap[y, x] == '#':
                x0 = max(0, x-1)
                x1 = min(x_dim, x+1)
                y0 = max(0, y-1)
                y1 = min(y_dim, y+1)

                window = seatmap[y0:y1+1, x0:x1+1]
                empty = np.count_nonzero(window=='L')
                filled = np.count_nonzero(window=='#') - 1 # Subtract current seat
                floor = np.count_nonzero(window=='.')

                if filled >= 4:
                    seatmap_new[y, x] = 'L'

    return seatmap_new

def count_visible(seatmap, x, y):
    incs = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
            [1, 1],
            [1, -1],
            [-1, 1],
            [-1, -1],
            ]
    
    filled = 0
    for inc in incs:
        xi = x
        yi = y

        while True:
            xi = xi + inc[1]
            yi = yi + inc[0]
            
            # Index out of range
            if xi < 0 or xi >= seatmap.shape[1] or yi < 0 or yi >= seatmap.shape[0]:
                break

            s = seatmap[yi, xi]
            
            if s == '#': # See a filled seat
                filled += 1
                break
            elif s == 'L': # See an empty seat
                break
    return filled


def change2(seatmap):
    seatmap_new = seatmap.copy()
    y_dim, x_dim = seatmap.shape
    for y in range(y_dim):
        for x in range(x_dim):
            if seatmap[y, x] == 'L':
                filled = count_visible(seatmap, x, y)
                if filled == 0:
                    seatmap_new[y, x] = '#'
            
            if seatmap[y, x] == '#':
                filled = count_visible(seatmap, x, y)
                if filled >= 5:
                    seatmap_new[y, x] = 'L'

    return seatmap_new



def part2(seatmap):
    count = 0
    while True:
        print(seatmap)
        print('Count: ', count)
        count += 1
        seatmap_new = change2(seatmap)
        if np.array_equal(seatmap, seatmap_new):
            break
        else:
            seatmap = seatmap_new

    filled = np.count_nonzero(seatmap=='#') # Subtract current seat
    print(filled)





seatmap = parse()

seatmap = part2(seatmap)

