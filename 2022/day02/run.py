
with open('input.txt', 'r') as f:
    lines = f.readlines()

map1 = {'A X': 4, 'B X': 1, 'C X': 7, 'A Y': 8, 'B Y': 5, 'C Y': 2, 'A Z': 3, 'B Z': 9, 'C Z': 6}

map2 = {'A X': 3, 'B X': 1, 'C X': 2, 'A Y': 4, 'B Y': 5, 'C Y': 6, 'A Z': 8, 'B Z': 9, 'C Z': 7}

score1 = 0
score2 = 0
for l in lines:
    l = l.rstrip()

    score1 += map1[l]

    score2 += map2[l]

print('Part 1: {}'.format(score1))
print('Part 2: {}'.format(score2))

