
with open('input.txt', 'r') as f:
    lines = f.read()

groups = lines.split('\n\n')

total = 0

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i, group in enumerate(groups):
    group_str = group.replace('\n', '')
    people = group.split('\n')
    num = len(people)
    
    #group = group.replace('\n', '')
    print(i)
    print(people)
    #for j in len(people):
    #    people[j] = set(people[j])

    
    for j, l in enumerate(letters):
        n = group_str.count(l)
        print(letters[j], n, num)
        if n == num:
            total += 1

print(total)















