from time import time as time
from functools import cache
designs = []

with open('input', 'r') as f:
    for line in f:
        if line == '\n': continue
        if ',' in line:
            patterns = line.strip().split(', ')
        else:
            designs.append(line.strip())

def recurse(design, patterns, depth=0):
    for pattern in patterns:
        if pattern in design:
            if design[depth:].startswith(pattern):
                if depth + len(pattern) == len(design):
                    return True
                if recurse(design, patterns, depth + len(pattern)):
                    return True

@cache
def recurse_ways(design, patterns):
    if not design: return 1
    return sum(recurse_ways(design[len(pattern):], patterns) for pattern in patterns if design.startswith(pattern))


possible_designs = set()
start_time = time()
for design in designs:
    if recurse(design, patterns):
        possible_designs.add(design)
print('Part1 answer:')
print(len(possible_designs))
print('Time:')
print(time() - start_time)

ans2 = 0
start_time = time()
for design in possible_designs:
    ans2 += recurse_ways(design, tuple(patterns))

print('Part2 answer:')
print(ans2)
print('Time:')
print(time() - start_time)
