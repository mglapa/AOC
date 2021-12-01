import numpy as np

with open('input.txt', 'r') as f:
    lines = f.readlines()

ids = []
seats = []

for line in lines:
    line = line.rstrip()
    row = line[0:7]
    col = line[7:10]

    rowb = ''
    colb = ''
    for i in range(len(row)):
        if row[i] == 'B':
            rowb += '1'
        else:
            rowb += '0'

    for i in range(len(col)):
        if col[i] == 'R':
            colb += '1'
        else:
            colb += '0'

    rowi = int(rowb, 2)
    coli = int(colb, 2)
    
    print(row, rowi, col, coli)

    id = 8*rowi + coli
    ids.append(id)
    seats.append([id, rowi, coli])

seats = np.array(seats)
seats = np.sort(seats, axis=0)

print(seats)

for i in range(seats.shape[0]):
    #print(seats[i])
    if seats[i+1][0] - seats[i][0] != 1:
        print(seats[i], seats[i+1])
        break



















