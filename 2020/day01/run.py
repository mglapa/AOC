
with open('input.txt', 'r') as f:
    lines = f.readlines()

idx0 = 0
idx1 = 1

while True:
    val0 = int(lines[idx0])
    val1 = int(lines[idx1])
    tot = int(val0) + int(val1)
    if tot == 2020:
        print(idx0, idx1)
        print(val0, val1)
        print(val0*val1)

        break

    idx1 += 1
    if idx1 == len(lines):
        idx0 += 1
        idx1 = idx0 + 1













