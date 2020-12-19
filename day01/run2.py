
with open('input.txt', 'r') as f:
    lines = f.readlines()

idx0 = 0
idx1 = 1
idx2 = 2

while True:
    val0 = int(lines[idx0])
    val1 = int(lines[idx1])
    val2 = int(lines[idx2])
    
    tot = val0 + val1 + val2
    if tot == 2020:
        print(idx0, idx1, idx2)
        print(val0, val1, val2)
        print(val0*val1*val2)

        break

    idx2 += 1
    if idx2 == len(lines):
        idx1 += 1
        idx2 = idx1 + 1

    if idx1 == len(lines)-1:
        idx0 += 1
        idx1 = idx0 + 1
        idx2 = idx1 + 1













