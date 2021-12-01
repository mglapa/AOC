
from math import sin, cos, radians, degrees, sqrt, atan

def parse():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    return lines

def part1(lines):
    angle = 0
    x = 0
    y = 0
    for line in lines:
        instr = line[0]
        num = int(line[1:])

        if instr == 'F':
            x += num*int(cos(radians(angle)))
            y += num*int(sin(radians(angle)))
        if instr == 'R':
            angle -= num
        if instr == 'L':
            angle += num
        if instr == 'N':
            y += num
        if instr == 'S':
            y -= num
        if instr == 'E':
            x += num
        if instr == 'W':
            x -= num

    dist = abs(x) + abs(y)
    print('Part 1: ', dist)

def get_angle(x, y, wp_x, wp_y):
    if wp_x == 0:
        if wp_y > 0:
            angle = 90
        else:
            angle = -90
    else:
        angle = degrees(atan(wp_y/wp_x))
        if wp_x < 0:
            angle += 180
    return angle


def part2(lines):
    x = 0
    y = 0
    wp_x = 10
    wp_y = 1
    for line in lines:
        instr = line[0]
        num = int(line[1:])

        if instr == 'F':
            x += num*wp_x
            y += num*wp_y

        if instr == 'R':
            dist = sqrt(wp_x**2 + wp_y**2)
            angle = get_angle(x, y, wp_x, wp_y) - num
            wp_x = round(dist*cos(radians(angle)))
            wp_y = round(dist*sin(radians(angle)))

        if instr == 'L':
            dist = sqrt(wp_x**2 + wp_y**2)
            angle = get_angle(x, y, wp_x, wp_y) + num
            wp_x = round(dist*cos(radians(angle)))
            wp_y = round(dist*sin(radians(angle)))

        if instr == 'N':
            wp_y += num
        if instr == 'S':
            wp_y -= num
        if instr == 'E':
            wp_x += num
        if instr == 'W':
            wp_x -= num

    dist = abs(x) + abs(y)
    print('Part 2: ', round(dist))



lines = parse()

part1(lines)

import time
t0 = time.time()
part2(lines)
t1 = time.time()

print(t1-t0)



