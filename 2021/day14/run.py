
import time
import regex as re
from itertools import permutations

#fn = 'sample.txt'
fn = 'input.txt'

def load():
    with open(fn, 'r') as f:
        lines = f.read()

    lines = lines.split('\n\n')

    template = lines[0]

    rules_dict = {}
    rules = lines[1].rstrip().split('\n')
    for i in range(len(rules)):
        rules[i] = rules[i].split(' -> ')
        rules_dict[rules[i][0]] = rules[i][1]

    return template, rules_dict

def part1():
    template, rules = load()

    # Create set of all possible letters
    letters = set()
    for key, insert in rules.items():
        letters.add(key[0])
        letters.add(key[1])
    for c in template:
        letters.add(c)

    # Run 10 times
    for s in range(10):
        # Log changes to a dict to be performed after the step
        changes = {}

        # Iterate through rules
        for key, insert in rules.items():
            # Find all locations of key in the string
            for ind in re.finditer(key, template, overlapped=True):
                changes[ind.start()] = insert

        # Iterate through changes and apply them
        for k in sorted(changes.keys(), reverse=True):
            template = template[:k+1] + changes[k] + template[k+1:]
        
    # Count each letter
    counts = []
    for c in letters:
        counts.append(template.count(c))
    
    print('Part 1: ', max(counts) - min(counts))

def part2():
    template, rules = load()

    # Create dict to track counts of each pair
    pairs = {}

    # Init dict with current pair counts
    for i in range(len(template)-1):
        pair = template[i:i+2]
        if pair not in pairs.keys():
            pairs[pair] = 1
        else:
            pairs[pair] += 1

    # Run 40 iterations
    for i in range(40):
        # Create copy of dict to log changes
        pairs_new = pairs.copy()
        
        # Iterate through pair count dict
        for k in pairs.keys():

            # If there is a rule for this key adjust pair counts by
            # subtracting the number of pair counts from the matching key
            # and adding to the number of new keys
            # i.e. NN -> (NC, CN)
            if k in rules.keys():
                pair1 = k[0] + rules[k]
                pair2 = rules[k] + k[1]

                if pair1 not in pairs_new.keys():
                    pairs_new[pair1] = 0
                if pair2 not in pairs_new.keys():
                    pairs_new[pair2] = 0
                
                pairs_new[pair1] += pairs[k]
                pairs_new[pair2] += pairs[k]
                pairs_new[k] -= pairs[k]

        # Apply changes from pairs_new to pairs
        pairs = pairs_new

    # After running 40 iterations, count the number of actual characters
    counts = {}
    for k, val in pairs.items():
        l1 = k[0]
        l2 = k[1]

        if l1 not in counts.keys():
            counts[l1] = 0
        if l2 not in counts.keys():
            counts[l2] = 0

        counts[l1] += val
        counts[l2] += val

    # Adjust the counts for the first and last letter of the template
    counts[template[0]] += 1
    counts[template[-1]] += 1

    # Divide counts by 2
    # (Every letter is in 2 pairs except the first and last)
    counts_arr = []
    for k in counts.keys():
        counts[k] /= 2
        counts_arr.append(int(counts[k]))

    print('Part 2: ', max(counts_arr) - min(counts_arr))

def main():
    
    part1()

    part2()


if __name__ == '__main__':
    main()    























