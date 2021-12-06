
import numpy as np

def load():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    data = []
    for i in range(len(lines)):
        lines[i] = lines[i].split(' ')
        x1, y1 = lines[i][0].split(',')
        x2, y2 = lines[i][2].split(',')
        data.append([int(x1), int(y1), int(x2), int(y2)])
    
    return np.array(data)

def part1():
    data = load()
    
    x_max = max(data[:,0].max(), data[:,2].max())
    y_max = max(data[:,1].max(), data[:,3].max())

    coords = np.zeros((x_max+2, y_max+2))

    for x1, y1, x2, y2 in data:
        if y1 == y2:
            coords[y1, min(x1, x2):max(x1, x2)+1] += 1
        if x1 == x2:
            coords[min(y1, y2):max(y1, y2)+1, x1] += 1

    print('Part 1: ', len(coords[coords >= 2]))



def part2():
    data = load()
    
    x_max = max(data[:,0].max(), data[:,2].max())
    y_max = max(data[:,1].max(), data[:,3].max())

    coords = np.zeros((x_max+2, y_max+2))

    for x1, y1, x2, y2 in data:
        if y1 == y2:
            coords[y1, min(x1, x2):max(x1, x2)+1] += 1
        elif x1 == x2:
            coords[min(y1, y2):max(y1, y2)+1, x1] += 1
        else:
            x = x1
            y = y1
            x2 = x2+1 if x2>x1 else x2-1
            y2 = y2+1 if y2>y1 else y2-1
            xd = 1 if x2>x1 else -1
            yd = 1 if y2>y1 else -1

            for x, y in zip(range(x1, x2, xd), range(y1, y2, yd)):
                coords[y, x] += 1
    
    print('Part 2: ', len(coords[coords >= 2]))



def main():
    
    part1()

    part2()


if __name__ == '__main__':
    main()    























