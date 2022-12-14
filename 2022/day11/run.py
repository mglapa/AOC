
import numpy as np

with open('input.txt', 'r') as f:
    lines = f.read()

class Monkey:
    def __init__(self, text, mode):
        self.lines = text.split('\n')
        self.mode = mode

    def reset(self):
        self.items = [int(x.replace(',', '')) for x in self.lines[1].split(' ')[4:]]
        self.div = int(self.lines[3].split(' ')[-1])
        self.throw1 = int(self.lines[4].split(' ')[-1])
        self.throw2 = int(self.lines[5].split(' ')[-1])
        self.N = 0
        
        self.op = None
        self.val = 0
        if self.lines[2].count('old')==2:
            self.op = 'square'
        elif '*' in self.lines[2]:
            self.op = 'mult'
            self.val = int(self.lines[2].split(' ')[-1])
        elif '+' in self.lines[2]:
            self.op = 'add'
            self.val = int(self.lines[2].split(' ')[-1])

    def get_item(self):
        if len(self.items) == 0:
            return None, None

        self.N += 1

        item = self.items.pop(0)
        if self.op == 'square':
            item = item**2
        elif self.op == 'mult':
            item *= self.val
        elif self.op == 'add':
            item += self.val

        if self.mode == 0:
            item = int(item/3)
        else:
            item = item % self.prod

        if item % self.div == 0:
            return item, self.throw1
        else:
            return item, self.throw2

    def print(self):
        print()
        print('items:       {}'.format(self.items))
        print('op:          {}'.format(self.op))
        print('val:         {}'.format(self.val))
        print('divisible:   {}'.format(self.div))
        print('true throw:  {}'.format(self.throw1))
        print('false throw: {}'.format(self.throw2))

def run(lines, N, mode):
    monkeys = []
    for l in lines:
        m = Monkey(l, mode)
        m.reset()
        monkeys.append(m)

    prod = np.prod([m.div for m in monkeys])
    for m in monkeys:
        m.prod = prod

    counts = []
    for i in range(N):
        for m in monkeys:
            while True:
                item, throw = m.get_item()
                if item == None:
                    break

                monkeys[throw].items.append(item)

    counts = []
    for m in monkeys:
        counts.append(m.N)
    
    counts = sorted(counts, reverse=True)

    return counts[0]*counts[1]

lines = lines.split('\n\n')

print('Part 1: {}'.format(run(lines, 20, 0)))

print('Part 2: {}'.format(run(lines, 10000, 1)))








