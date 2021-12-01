
import numpy as np
from scipy.ndimage.filters import convolve

def parse():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    # Get cubes into numpy array
    cubes = []
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].replace('.', '0')
        lines[i] = lines[i].replace('#', '1')
        cubes.append([x for x in lines[i].rstrip()])
    cubes = np.array(cubes)
    return cubes

def part1(cubes):
    # Init large 3D space
    dim = 21
    space = np.zeros((dim, dim, dim), dtype=np.int)

    # Copy initial state to center of 3D space
    x, y = cubes.shape
    half = (dim // 2) - x//2
    x += half
    y += half
    space[dim//2, half:x, half:y] = cubes
    
    # Init 3D kernel
    kernel = np.ones((3, 3, 3), dtype=np.int)
    kernel[1, 1, 1] = 0

    # Run through 6 rounds
    for i in range(6):
        neighbors = convolve(space, kernel)
        
        inact = np.where(space==0)
        act = np.where(space==1)
        for x, y, z in zip(act[0], act[1], act[2]):
            if neighbors[x, y, z] != 2 and neighbors[x, y, z] != 3:
                space[x, y, z] = 0

        for x, y, z in zip(inact[0], inact[1], inact[2]):
            if neighbors[x, y, z] == 3:
                space[x, y, z] = 1

    unique, counts = np.unique(space, return_counts=True)
    active = counts[1]
    print('Part 1: ', active)

def part2(cubes):
    # Init large 4D space
    dim = 18
    space = np.zeros((dim, dim, dim, dim), dtype=np.int)

    # Copy initial state to center of 4D space
    x, y = cubes.shape
    half = (dim // 2) - x//2
    x += half
    y += half
    space[dim//2, dim//2, half:x, half:y] = cubes
    
    # Init 4D conv kernel
    kernel = np.ones((3, 3, 3, 3), dtype=np.int)
    kernel[1, 1, 1, 1] = 0

    # Run through 6 rounds
    for i in range(6):
        neighbors = convolve(space, kernel)
        
        inact = np.where(space==0)
        act = np.where(space==1)
        for x, y, z, a in zip(act[0], act[1], act[2], act[3]):
            if neighbors[x, y, z, a] != 2 and neighbors[x, y, z, a] != 3:
                space[x, y, z, a] = 0

        for x, y, z, a in zip(inact[0], inact[1], inact[2], inact[3]):
            if neighbors[x, y, z, a] == 3:
                space[x, y, z, a] = 1

    unique, counts = np.unique(space, return_counts=True)
    active = counts[1]
    print('Part 2: ', active)

cubes = parse()

part1(cubes)

import time

t0 = time.time()
part2(cubes)
t1 = time.time()

print(t1-t0)











