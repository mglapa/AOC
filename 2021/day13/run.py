
import numpy as np

#fn = 'sample.txt'
fn = 'input.txt'

def load():
    with open(fn, 'r') as f:
        lines = f.read()
    
    lines = lines.split('\n\n')

    pts = lines[0]


    pts = pts.split('\n')
    for i in range(len(pts)):
        pts[i] = pts[i].split(',')
        pts[i] = [int(pts[i][0]), int(pts[i][1])]
    
    #pts = np.array(pts, dtype=np.int)

    folds = lines[1]
    folds = folds.split('\n')

    return pts, folds

def part1():
    pts, folds = load()

    for f in folds:
        if f=='':
            break

        f = f.split(' ')
        dim = f[2].split('=')[0]
        idx = int(f[2].split('=')[1])
        
        for i in range(len(pts)):
            if dim=='y' and pts[i][1] > idx:
                pts[i][1] = idx - (pts[i][1] - idx)
            if dim=='x' and pts[i][0] > idx:
                pts[i][0] = idx - (pts[i][0] - idx)

        folded = []
        for p in pts:
            if p not in folded:
                folded.append(p)

        pts = folded

        break


def part2():
    pts, folds = load()

    for f in folds:
        if f=='':
            break

        f = f.split(' ')
        dim = f[2].split('=')[0]
        idx = int(f[2].split('=')[1])
        
        for i in range(len(pts)):
            if dim=='y' and pts[i][1] > idx:
                pts[i][1] = idx - (pts[i][1] - idx)
            if dim=='x' and pts[i][0] > idx:
                pts[i][0] = idx - (pts[i][0] - idx)

        folded = []
        for p in pts:
            if p not in folded:
                folded.append(p)

        pts = folded

    xmax = 0
    ymax = 0
    for x,y in pts:
        xmax = max(x, xmax)
        ymax = max(y, ymax)

    print(xmax, ymax)

    disp = np.ones((ymax+1, xmax+1), np.int)
    #disp[:,:] = ' '

    for x,y in pts:
        disp[y, x] = 0

    lines = []
    line = '{:1}'*(xmax+1)

    for idx in range(disp.shape[0]):
        l = line.format(*disp[idx])
        l = l.replace('1', ' ')
        print(l)

def main():
    
    part1()

    part2()


if __name__ == '__main__':
    main()    























