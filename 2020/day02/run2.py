
with open('input.txt', 'r') as f:
    lines = f.readlines()


count = 0
for line in lines:
    line = line.split(' ')
    
    idx0 = int(line[0].split('-')[0])
    idx1 = int(line[0].split('-')[1])

    l = line[1][0]

    word = line[2].rstrip()

    l0 = word[idx0-1]
    l1 = word[idx1-1]

    check = 0
    if l0 == l:
        check += 1
    if l1 == l:
        check += 1

    if check == 1:
        count += 1

    
print('total: ', count)


