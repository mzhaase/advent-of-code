"""
Part 1:
Given a map of points of different types, find the number of points
that are on a straight line between any two points of the same type, and
are d distance away from one point and 2d distance away from the other

Part 2:
Same, but don't care about distance, instead everything that is on a straight
line
"""

import itertools
import math

from time import time as time

debug = False
if debug: antennae_map = []
antennae = {}
with open('./input', 'r') as f:
    for y, line in enumerate(f):
        if debug: antennae_map.append([])
        for x, char in enumerate(line.strip()):
            if debug: antennae_map[y].append(char)
            if not char == '.':
                if char not in antennae:
                    antennae[char] = []
                antennae[char].append((x, y))
    x_limit = x
    y_limit = y

def get_coefficients(point_a, point_b):
    """For two points on a plane, return the coefficients of the line that
    passes through both points

    Args:
        point_a (tuple): (x1, y1)
        point_b (tuple): (x2, y2)

    Returns:
        int, int: m, b where f(x) = mx + b
    """
    x1, y1 = point_a
    x2, y2 = point_b
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b

def get_distance(point_a, point_b):
    """Returns cartesian distance between two points

    Args:
        point_a (tuple): (x1, y1)
        point_b (tuple): (x2, y2)

    Returns:
        float: distance
    """
    x1, y1 = point_a
    x2, y2 = point_b
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_antinodes(point_a, point_b):
    # an antinode is defined to be a point that is on a straight line defined
    # by two points, where one point is twice as far away from the antinode as
    # the other
    # ex
    # 0 . . A . A . . 0
    # if 4 away from one A and 2 away from the other A
    x1, y1 = point_a
    x2, y2 = point_b
    m, b = get_coefficients(point_a, point_b)
    distance = get_distance(point_a, point_b)
    x_offset = distance / math.sqrt(1 + m**2)
    antinodes = set()
    # there are two solutions for every antinode, but the antinodes have to be
    # 'outside' the two points
    if x1 < x2:
        antinodes.update((
            (int(x1 - x_offset), int(m * (x1 - x_offset) + b)),
            (int(x2 + x_offset), int(m * (x2 + x_offset) + b))
        ))
    else:
        antinodes.update((
            (int(x1 + x_offset), int(m * (x1 + x_offset) + b)),
            (int(x2 - x_offset), int(m * (x2 - x_offset) + b))
        ))
    return antinodes

def get_antinodes_repeating(point_a, point_b):
    # this time, we don't care about the distance
    # using linear functions worked for part 1, but here it does not add up due
    # to floating point errors
    # instead if we have two points, we just check their x and y distance and
    # repeat antinodes in that pattern
    x1, y1 = point_a
    x2, y2 = point_b
    dx, dy = x2 - x1, y2 - y1
    x, y = x1, y1
    
    antinodes = set()
    while x <= x_limit and y <= y_limit:
        antinodes.add((x, y))
        x += dx
        y += dy
    
    x, y = x1, y1
    while x >= 0 and y >= 0:
        antinodes.add((x, y))
        x -= dx
        y -= dy
    return antinodes

def solve(part_two=False):
    antinodes = set()
    for frequency, antennas in antennae.items():
        # get all possible pairs of antennas of the same frequency
        antenna_combinations = list(itertools.combinations(antennas, 2))
        for antenna_pair in antenna_combinations:
            if part_two:
                antinodes.update(get_antinodes_repeating(*antenna_pair))
            else:
                antinodes.update(get_antinodes(*antenna_pair))
    answer = 0
    for antinode in antinodes:
        x, y = antinode
        if x < 0 or y < 0 or x > x_limit or y > y_limit:
            continue
        answer += 1
        if debug:
            antennae_map[y][x] = '#'
    if debug:
        output = ''
        for line in antennae_map:
            for char in line:
                output += char
            output += '\n'
        print(output)
    return answer

start_time = time()
print(f'Part 1 solution: {solve()}')
print(f'Execution time: {time() - start_time}')
start_time = time()
print(f'Part 2 solution: {solve(part_two=True)}')
print(f'Execution time: {time() - start_time}')
