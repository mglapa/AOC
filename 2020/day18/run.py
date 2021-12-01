
def parse():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip().replace(' ', '')
            #print(lines[i])

    return lines

def line_to_array(line):
    eq = []
    val = ''

    # Iterate through line - add numbers and symbols to array
    for x in line:
        if x.isnumeric():
            val += x
        else:
            if val:
                eq.append(int(val))
                val = ''
            eq.append(x)
    if val:
        eq.append(int(val))
    
    return eq

# Evaluate a line that doesn't have parentheses
def simple_eval(eq, mode):
    if mode == 0:
        # Start with first number
        val = eq[0]

        # Iterate through lines and get operation and value
        for i in range(2, len(eq), 2):
            if eq[i-1] == '*':
                val *= eq[i]
            elif eq[i-1] == '+':
                val += eq[i]
            else:
                print('wtf do i do with this: ', eq[i-1])
    if mode == 1:
        plus = True
        while plus:
            plus = False
            for i in range(2, len(eq), 2):
                print(eq)
                if eq[i-1] == '+':
                    plus = True
                    val = eq[i-2] + eq[i]
                    eq.insert(i+1, val)
                    eq.pop(i-2)
                    eq.pop(i-2)
                    eq.pop(i-2)
                    break
        

        val = simple_eval(eq, 0)

        '''
        for i in range(2, len(eq), 2):
            print(eq[i-2], eq[i-1], eq[i])
            if eq[i-1] == '*':
                val = eq[i-2] * eq[i]
                eq.insert(i+1, val)
                eq.pop(i-2)
                eq.pop(i-2)
                eq.pop(i-2)
        '''

    return val

# Function to extract simple expressions that don't have parentheses
def get_simple(line, mode):
    opn = 0
    close = 0
    
    eq = []
    new_eq = []

    for x in line:
        if not opn:
            if x != '(' and x != ')':
                new_eq.append(x)

        if x == ')':
            close += 1

        if opn and close and (opn-close)==0:
            if '(' in eq:
                #print('Simplify: ', eq)
                l = get_simple(eq, mode)
                #for l in lin:
                #    new_eq.append(l)
            else:
                # No parentheses - evaluate equation to get number
                #print('Simplified: ', eq)
                l = simple_eval(eq, mode)
            new_eq.append(l)
            eq = []
            opn = 0
            close = 0

        if opn:
            eq.append(x)
        if x == '(':
            opn += 1


    #print('simple eq: ', new_eq)
    new_eq = simple_eval(new_eq, mode)
    #print('ret: ', new_eq)
    return new_eq


def part1(lines):
    total = 0
    for line in lines:
        line = line_to_array(line)
        val = get_simple(line, mode=0)
        total += val
    print(total)

def part2(lines):
    total = 0
    for line in lines:
        line = line_to_array(line)
        val = get_simple(line, mode=1)
        total += val
    print(total)

lines = parse()

part1(lines)

part2(lines)




