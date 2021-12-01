
import numpy as np

def parse():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    t_earliest = int(lines[0])

    buses = []
    bus_idx = []
    for idx, x in enumerate(lines[1].rstrip().split(',')):
        if x.isnumeric():
            buses.append(int(x))
            bus_idx.append(idx)

    return t_earliest, buses, bus_idx


def part1(t_earliest, buses):
    times = []
    for b in buses:
        i = 0
        while True:
            if b*i > t_earliest:
                times.append(b*i)
                break
            i += 1
    
    t_wait = min(times) - t_earliest
    bid = buses[np.argmin(times)]

    print('Part 1: ', t_wait*bid)

def part2(buses, offsets):
    t = 0
    solved = [buses[0]]
    while True:
        print(t)
        for bid, off in zip(buses[1:], offsets[1:]):
            if (t+off) % bid == 0:
                print('woo: ', bid)
                if bid not in solved:
                    solved.append(bid)

                if len(solved) == len(buses):
                    print('Win: ', t)
                    exit()
                continue
            else:
                break

        t += np.product(solved)

t_earliest, buses, bus_idx = parse()

part1(t_earliest, buses)

part2(buses, bus_idx)








