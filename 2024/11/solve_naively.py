from copy import deepcopy
from math import ceil, log10
from time import time as time

import cProfile
import pstats

with open('./input', 'r') as f:
    stones = [int(i) for i in f.read().strip().split()]

def iterate_stones(iterations, stones):
    for i in range(iterations):
        print(f'Iteration {i}')
        # if len(stones) < 40: print(stones)
        idx = 0
        to_append = []
        while idx < len(stones):
            stone = stones[idx]
            number_of_digits = ceil(log10(stone + 1))
            if stone == 0:
                stones[idx] = 1
            elif stone > 1 and number_of_digits % 2 == 0:
                # split number into two equal parts
                # 1234 becomes 12 and 34
                # 1000 becomes 10 and 0
                # ceil log10 gives number of digits.
                # so by dividing by 10 ** number of digits we get the first half if
                # we ignore everything behind the decimal point
                divisor = 10 ** (number_of_digits // 2)
                stones[idx] = stone // divisor
                to_append.append(stone % divisor)
            else:
                stones[idx] = stone * 2024
            idx += 1
        stones += to_append
    return stones

start_time = time()
print(f'Part 1: {len(iterate_stones(25, deepcopy(stones)))}')
print(f'Execution time: {time() - start_time}')
start_time = time()
print(f'Part 2: {len(iterate_stones(75, deepcopy(stones)))}')
print(f'Execution time: {time() - start_time}')

# cProfile.run('iterate_stones(25, deepcopy(stones))', 'profile')
# p = pstats.Stats('profile')
# p.strip_dirs().sort_stats(-1).print_stats()