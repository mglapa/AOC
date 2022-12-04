
with open('input.txt', 'r') as f:
    lines = f.readlines()

count1 = 0
count2 = 0

for l in lines:
    p1, p2 = l.split(',')

    p1 = p1.split('-')
    p2 = p2.split('-')

    p1[0] = int(p1[0])
    p1[1] = int(p1[1])
    p2[0] = int(p2[0])
    p2[1] = int(p2[1])

    if ((p1[0] <= p2[0]) and (p1[1] >= p2[1])) or ((p2[0] <= p1[0]) and (p2[1] >= p1[1])):
        count1 += 1

    if (p1[0] <= p2[1] and p1[1] >= p2[0]) or (p1[1] >= p2[0] and p1[0] <= p2[1]):
        count2 += 1

print('Part 1: {}'.format(count1))
print('Part 2: {}'.format(count2))


