
with open('input.txt', 'r') as f:
    lines = f.readlines()


count = 0
for line in lines:
    line = line.split(' ')
    
    mini = int(line[0].split('-')[0])
    maxi = int(line[0].split('-')[1])

    l = line[1][0]

    word = line[2].rstrip()

    n = word.count(l)

    if n >= mini and n <= maxi:
        count += 1

    print(mini, maxi, l, word, n)
    
print('total: ', count)


