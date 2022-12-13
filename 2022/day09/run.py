
import numpy as np

with open('input.txt', 'r') as f:
    lines = f.readlines()

# Function for visualizing "input2.txt" example
def visualize(coords):

    xdim = 26
    ydim = 21

    disp = np.chararray((ydim, xdim), unicode=True)
    disp[:, :] = '.'

    for i, c in enumerate(coords):
        disp[c[1]+15, c[0]+11] = str(i)

    print()
    for d in disp:
        print(('{}'*xdim).format(*d))

def process(N):

    T_path2 = set()
    coords = np.zeros((N, 2), np.int32)

    for l in lines:
        d, n = l.strip().split(' ')

        for i in range(int(n)):
            if d == 'U':
                coords[0][1] -= 1
            if d == 'D':
                coords[0][1] += 1
            if d == 'L':
                coords[0][0] -= 1
            if d == 'R':
                coords[0][0] += 1

            for j in range(1, len(coords)):
                H = coords[j-1]
                T = coords[j]

                if abs(H[0]-T[0])>1 and abs(H[1]-T[1])>1:
                    T[0] += np.sign(H[0] - T[0])
                    T[1] += np.sign(H[1] - T[1])
                    continue

                if abs(H[0]-T[0])>1:
                    T[0] += np.sign(H[0] - T[0])
                    if abs(H[1]-T[1]) == 1:
                        T[1] += np.sign(H[1]-T[1])
                if abs(H[1]-T[1])>1:
                    T[1] += np.sign(H[1] - T[1])
                    if abs(H[0]-T[0]) == 1:
                        T[0] += np.sign(H[0]-T[0])

            T_path2.add(str(coords[-1]))

        #visualize(coords)

    return len(T_path2)

print('Part 1: {}'.format(process(2)))
print('Part 2: {}'.format(process(10)))


