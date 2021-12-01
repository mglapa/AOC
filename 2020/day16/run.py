
import numpy as np

def parse():
    with open('input.txt', 'r') as f:
        lines = f.read()
    
    sections = lines.split('\n\n')
    
    # Parse rules
    rules = {}
    rule_lines = sections[0].split('\n')
    for line in rule_lines:
        name, ranges = line.split(':')
        ranges = ranges.split(' ')
        min1, max1 = ranges[1].split('-')
        min2, max2 = ranges[3].split('-')
        rules[name] = [int(min1), int(max1), int(min2), int(max2)]

    ticket = sections[1].split('\n')[1]

    nearby = sections[2].split('\n')[1:-1]

    return rules, ticket, nearby

def part1(rules, ticket, nearby):
    bad = []
    bad_tickets = []
    for near in nearby:
        vals = near.split(',')
        for idx, n in enumerate(vals):
            n = int(n)
            good = False
            for key, ranges in rules.items():
                min1, max1, min2, max2 = ranges
                if ((n >= min1) and (n <= max1)) or ((n >= min2) and (n <= max2)):
                    good = True
                    break
            if good == False:
                bad.append(n)
                bad_tickets.append(near)

    print('Part 1: ', sum(bad))
    valid_tickets = []
    for t in nearby:
        if t not in bad_tickets:
            valid_tickets.append(t)

    return valid_tickets

def check_ranges(x, ranges):
    min1, max1, min2, max2 = ranges
    if (x >= min1 and x <= max1) or (x >= min2 and x <= max2):
        return True
    else:
        return False

def part2(rules, ticket, nearby):
    # Convert to numpy array so we can get columns
    tickets = []
    for near in nearby:
        near = near.split(',')
        tickets.append(near)
    tickets = np.array(tickets)

    print(tickets)
    
    fields = {}
    for key, ranges in rules.items():
        fields[key] = []
        for i in range(tickets.shape[1]):
            good = True
            for t in tickets[:, i]:
                ret = check_ranges(int(t), ranges)
                if not ret:
                    good = False
                    break
            if good == True:
                fields[key].append(i)

    print(fields)

    final_fields = {}
    while True:
        for key, vals in fields.items():
            if len(vals) == 1:
                # This is the only option: set this index in final_fields and remove from current dict
                final_fields[key] = vals[0]
                index = vals[0]
                del fields[key]

                # Dict cant change during iteration, so break and start over
                break
        
        # Remove this index as a possibility for other fields
        for key, vals in fields.items():
            fields[key] = [x for x in fields[key] if x != index]
            print(fields)


        if not fields:
            break

    print(final_fields)
    
    # Sort my ticket into fields
    ticket = ticket.split(',')
    ticket_sorted = {}
    for key, idx in final_fields.items():
        ticket_sorted[key] = ticket[final_fields[key]]

    print(ticket_sorted)

    mult = []
    for key, val in ticket_sorted.items():
        if 'departure' in key:
            mult.append(val)

    print(mult)

    m = 1
    for j in mult:
        m *= int(j)

    print(m)


rules, ticket, nearby = parse()

valid = part1(rules, ticket, nearby)

part2(rules, ticket, valid)


