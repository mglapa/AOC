
def priority(c):
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96

with open('input.txt', 'r') as f:
    lines = f.readlines()

total = 0
for l in lines:
    l1 = set(l[:(len(l)//2)])
    l2 = set(l[(len(l)//2):])
    
    c = l1.intersection(l2).pop()
    total += priority(c)

print('Part 1: {}'.format(total))

total2 = 0
for i in range(0, len(lines), 3):
    l1 = set(lines[i].rstrip())
    l2 = set(lines[i+1].rstrip())
    l3 = set(lines[i+2].rstrip())

    c = l1.intersection(l2, l3).pop()
    total2 += priority(c)

print('Part 2: {}'.format(total2))



