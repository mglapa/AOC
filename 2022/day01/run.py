
with open('input.txt', 'r') as f:
    lines = f.read()

elves = lines.split('\n\n')

counts = []
for i in range(len(elves)):
    
    elf = elves[i].rstrip().split('\n')
    
    total = 0
    for c in elf:
        total += int(c)

    counts.append(total)

print('part 1: {}'.format(max(counts)))

counts = sorted(counts, reverse=True)
top3 = sum(counts[:3])

print('part 2: {}'.format(top3))

