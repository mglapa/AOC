
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

def part1_2():
    lines = load()

    # Number of objects in grid
    num = lines.shape[0] * lines.shape[1]
    
    total = 0
    for i in range(500):
        
        # List to track all flashed indices
        flashed = []
        
        # Increment all values
        lines += 1
        
        # Find indices of all values over 9
        idx = np.where(lines>9)

        # Keep repeating as long as there are more flashing indices
        while len(idx[0]) != 0:
            # Iterate through values over 9
            for y, x in zip(idx[0], idx[1]):
                # Add index to 'flashed' list
                flashed.append([x, y])
                # Iterate through neighbors
                for xd in [-1, 0, 1]:
                    for yd in [-1, 0, 1]:
                        x0 = x+xd
                        y0 = y+yd
                        # Skip out of bounds indices
                        if x0 < 0 or x0 >= lines.shape[1] or y0 < 0 or y0 >= lines.shape[0]:
                            continue
                        
                        # Increment neighbors, but ignore values that have already flashed
                        if [x0, y0] not in flashed:
                            lines[y0, x0] += 1

            # Set all 'flashed' values to zero
            for x, y in flashed:
                lines[y, x] = 0
            
            # Find secondary flashes in this step
            idx = np.where(lines>9)
            
            # If check if number of flashed objects == size of grid
            if len(flashed) == (lines.shape[0] * lines.shape[1]):
                print('Part 2: ', i+1)
                return

        # Add to total flashed count
        total += len(flashed)
        if i == 99:
            print('Part 1: ', total)

def main():
    part1_2()

if __name__ == '__main__':
    main()    























