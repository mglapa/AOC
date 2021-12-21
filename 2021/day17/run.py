
import numpy as np

#fn = 'sample.txt'
fn = 'input.txt'

def load():
    with open(fn, 'r') as f:
        lines = f.readlines()

    line = lines[0].rstrip().replace(',', '').split(' ')

    xdim = line[2].replace('x=', '').split('..')
    ydim = line[3].replace('y=', '').split('..')

    x1 = int(xdim[0])
    x2 = int(xdim[1])

    y1 = int(ydim[0])
    y2 = int(ydim[1])

    return [x1, x2, y1, y2]

def check_target(x, y, target):
    if x > target[1] or y < target[2]:
        return -1
    elif x >= target[0] and x <= target[1] and y >= target[2] and y <= target[3]:
        return 1
    else:
        return 0

def test(vx, vy, target):
    xpos = 0
    ypos = 0
    ymax = ypos

    for s in range(1000):
        xpos += vx
        ypos += vy
        ymax = max(ymax, ypos)

        #print('{:3d}  {:3d}  |  {:3d}  {:3d}  |  {:3d}  {:3d}  {:3d}  {:3d}'
        #    .format(xpos, ypos, vx, vy, *target))

        ret = check_target(xpos, ypos, target)
        if ret != 0:
            return ret, ymax

        if vx > 0:
            xsign = 1
        elif vx < 0:
            xsign = -1
        else:
            xsign = 0

        vx -= xsign
        vy -= 1

    return -1, ymax

def part1():
    target = load()

    best = -1e10
    init = []

    for i in range(1000000):

        vx = np.random.randint(0, 300)
        vy = np.random.randint(-200, 200)

        ret, ymax = test(vx, vy, target)

        if ret == 1:
            best = max(ymax, best)
            if [vx, vy] not in init:
                init.append([vx, vy])
            
        print(best, len(init))


def part2():
    target = load()


def main():
    
    part1()

    part2()


if __name__ == '__main__':
    main()    























