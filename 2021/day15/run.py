
import numpy as np

#fn = 'sample.txt'
fn = 'input.txt'

def load():
    with open(fn, 'r') as f:
        lines = f.readlines()
    
    for i in range(len(lines)):
        lines[i] = list(lines[i].rstrip())

    lines = np.array(lines, np.int)
    
    return lines

def get_neighbors(x, y, grid):
    a = []
    h, w = grid.shape
    for delta in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        xd = x + delta[0]
        yd = y + delta[1]
        if xd < 0 or xd >= w:
            continue
        if yd < 0 or yd >= h:
            continue
        a.append([xd, yd])
    return a

def traverse(grid):
    risks = 1e10 * np.ones_like(grid)

    checklist = [[0, 0]]
    risks[0,0] = 0
    while True:
        try:
            x, y = checklist.pop(0)
        except:
            break
        neighbors = get_neighbors(x, y, grid)
        for xn, yn in neighbors:
            temp = risks[y, x] + grid[yn, xn]
            if risks[y, x] + grid[yn, xn] < risks[yn, xn]:
                risks[yn, xn] = risks[y, x] + grid[yn, xn]
                checklist.append([xn, yn])
       
    return risks[-1, -1]
        


def part1():
    grid = load()
    risk = traverse(grid)    
    print('Part 1: ', risk)


def tile(grid):

    h_grids = []
    for i in range(5):
        tmp_grid = grid.copy()
        tmp_grid += i
        tmp_grid[tmp_grid>=10] %= 9
        h_grids.append(tmp_grid)

    grid = np.concatenate(h_grids, axis=1)

    v_grids = []
    for i in range(5):
        tmp_grid = grid.copy()
        tmp_grid += i
        tmp_grid[tmp_grid>=10] %= 9
        v_grids.append(tmp_grid)

    grid = np.concatenate(v_grids, axis=0)

    return grid
    #np.set_printoptions(linewidth=500)
    #print(grid)


def part2():
    grid = load()

    grid = tile(grid)

    risk = traverse(grid)
    print('Part 2: ', risk)





def main():
    
    part1()

    part2()


if __name__ == '__main__':
    main()    























