
with open('input.txt', 'r') as f:
    lines = f.read()

groups = lines.split('\n\n')

total = 0

for i, group in enumerate(groups):
    group = group.replace('\n', '')
    group = ''.join(set(group))
    total += len(group)

print(total)















