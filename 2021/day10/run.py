
import numpy as np

#fn = 'sample.txt'
fn = 'input.txt'

def load():
    with open(fn, 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def is_open(c):
    if c == '[' or c == '(' or c == '{' or c == '<':
        return True
    return False

def is_close(c):
    if c == ']' or c == ')' or c == '}' or c == '>':
        return True
    return False

def is_complete(c1, c2):
    if (c1 == '[' and c2 == ']'):
        return True
    if (c1 == '(' and c2 == ')'):
        return True
    if (c1 == '{' and c2 == '}'):
        return True
    if (c1 == '<' and c2 == '>'):
        return True
    return False

def get_score(c):
    if c == ')':
        return 3
    if c == ']':
        return 57
    if c == '}':
        return 1197
    if c == '>':
        return 25137

def find_corrupt_lines(lines):
    score = 0
    bad = []
    for i, l in enumerate(lines):
        opens = []
        for c in l:
            if is_open(c):
                opens.append(c)
            if is_close(c):
                if is_complete(opens[-1], c):
                    opens.pop(-1)
                else:
                    bad.append(i)
                    score += get_score(c)
                    break

    return score, bad

def part1():
    lines = load()

    score, _ = find_corrupt_lines(lines)

    print('Part 1: ', score)


def part2():
    
    lines = load()

    # Find and remove corrupt lines
    _, bad_lines = find_corrupt_lines(lines)
    bad_lines = sorted(bad_lines, reverse=True)
    for i in bad_lines:
        lines.pop(i)
    
    # Iterate through lines and find brackets that aren't closed
    scores = []
    for i, l in enumerate(lines):
        opens = []
        for c in l:
            if is_open(c):
                opens.append(c)
            if is_close(c):
                if is_complete(opens[-1], c):
                    opens.pop(-1)

        # Reverse open bracket list - closed brackets should appear in reverse order
        opens.reverse()
        
        # Calculate score for each bracket
        score = 0
        for o in opens:
            if o == '(':
                score = (5*score) + 1
            if o == '[':
                score = (5*score) + 2
            if o == '{':
                score = (5*score) + 3
            if o == '<':
                score = (5*score) + 4

        scores.append(score)

    # Sort scores and find 'middle' value
    scores = sorted(scores)
    final = scores[len(scores)//2]

    print('Part 2: ', final)
   

def main():
    
    part1()

    part2()


if __name__ == '__main__':
    main()    























