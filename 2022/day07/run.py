
with open('input.txt', 'r') as f:
    lines = f.readlines()

# Init root filesystem
root = {}

# Iterate through commands and store files and dirs
i = 0
while i < len(lines):

    # List files in directory
    if lines[i].strip() == '$ ls':
        # Iterate through following lines until another command or EOF
        while True:
            i += 1
            if (i >= len(lines)) or ('$' in lines[i]):
                break
            else:
                mode, name = lines[i].strip().split(' ')
                if mode == 'dir':
                    cur[name] = {'..': cur}
                else:
                    cur[name] = int(mode)
    
    if i >= len(lines):
        break

    # Set current directory to root
    if lines[i].strip() == '$ cd /':
        cur = root

    # Change current directory
    elif lines[i].strip()[:4] == '$ cd':
        new = lines[i].strip().split(' ')[-1]
        cur = cur[new]

    i += 1

# Recursive function for traversing through tree
# and calculating directory sizes for Part 1
part1 = 0
def get_size(tree):
    global part1
    total = 0
    for k, v in tree.items():
        if isinstance(v, dict):
            if k != '..':
                total += get_size(v)
        else:
            total += v

    if total <= 100000:
        part1 += total

    return total

# Traverse tree and print
used = get_size(root)
print('Part 1: {}'.format(part1))

# Part 2 requirements
part2 = 1e20
disk_size = 70000000
required = 30000000
diff = used + required - disk_size

# Recursive function for traversing through tree
# and calculating minimum dir for deletion for Part 2
def get_size2(tree):
    global part2
    total = 0
    for k, v in tree.items():
        if isinstance(v, dict):
            if k != '..':
                total += get_size2(v)
        else:
            total += v

    if total >= diff and total <= part2:
        part2 = total

    return total

# Traverse tree again and print
get_size2(root)
print('Part 2: {}'.format(part2))

