from copy import deepcopy
from collections import defaultdict
from math import ceil, log10
from time import time as time

# new idea. there will be repeated numbers. we only have to solve once for every
# unique number, and keep track how often that number appears

# workaround to have a defaultdict that is per default the integer 0
stones = defaultdict(lambda: 0)

# create dict of form
# stoneid: frequency
with open('./input', 'r') as f:
    for line in f:
        for char in line.strip().split(' '):
            stones[int(char)] += 1

def iterate(iterations, stones):
    for i in range(iterations):
        _ = defaultdict(lambda: 0)
        for stone in stones.keys():
            number_of_digits = ceil(log10(stone + 1))
            if stone == 0:
                _[1] += stones[stone]
            elif stone > 1 and number_of_digits % 2 == 0:
                divisor = 10 ** (number_of_digits // 2)
                _[stone // divisor] += stones[stone]
                _[stone % divisor] += stones[stone]
            else:
                _[stone * 2024] += stones[stone]
        stones = deepcopy(_)
    ans = 0
    for k, v in stones.items():
        ans += v
    return ans

start_time = time()
print(f'Part 1: {iterate(25, deepcopy(stones))}')
print(f'Execution time: {time() - start_time}')
start_time = time()
print(f'Part 2: {iterate(75, deepcopy(stones))}')
print(f'Execution time: {time() - start_time}')