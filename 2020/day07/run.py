
def parse_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    rules = {}

    for line in lines:
        line = line.rstrip().split(' ')
        outer = line[0] + '_' + line[1]
        inner = []
        for i in range(10):
            try:
                idx = 4*(i+1)
                num = line[idx]
                if num == 'no':
                    num = 0
                else:
                    num = int(num)

                typ = line[idx+1] + '_' + line[idx+2]
                
                b = [num, typ]
                inner.append(b)
            except:
                break

        rules[outer] = inner

    return rules

def part1(rules):
    # Start searching
    check = ['shiny_gold']
    found = []

    for c in check:
        for key in rules.keys():
            for num, typ in rules[key]:
                if c in typ:
                    if key not in found:
                        found.append(key)
                    check.append(key)
    
    print('Part 1: ', len(found))

def rec(rules, key):
    # Check num for first bag
    # If zero, it's the end of the branch
    if rules[key][0][0] == 0:
        return 0
    else:
        count = 0
        for num, typ in rules[key]:
            bags = rec(rules, typ)
            count += num*bags + num
        return count


def part2(rules):
    count = rec(rules, 'shiny_gold')
    print('Part 2: ', count)

rules = parse_input()

part1(rules)

part2(rules)














