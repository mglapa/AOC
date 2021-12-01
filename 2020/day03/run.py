
with open('input.txt', 'r') as f:
    lines = f.readlines()


for i in range(len(lines)):
    lines[i] = 1000*lines[i].rstrip()

paths = [
            [1, 1],
            [3, 1],
            [5, 1],
            [7, 1],
            [1, 2]
        ]

counts = []
for i, path in enumerate(paths):
    x = 0
    y = 0
    counts.append(0)
    while True:
        try:
            val = lines[y][x]
        except:
            break

        if val == '#':
            counts[i] += 1
        
        x += path[0]
        y += path[1]

print(counts)

prod = 1
for n in counts:
    prod *= n

print(prod)




