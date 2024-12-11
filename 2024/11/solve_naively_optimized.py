from copy import deepcopy
from math import ceil, log10
from time import time as time

import cProfile
import pstats

with open('./input', 'r') as f:
    stones = [int(i) for i in f.read().strip().split()]

# optimization idea:
# 0s are going to be very common every time the list grows.
# lets pre-calculate how many stones a 0 becomes after a number of iterations
# then whenever a 0 shows up in the list we can just remove that 0 and keep a
# counter how often it happened

def apply_rules(stone):
    number_of_digits = ceil(log10(stone + 1))
    if stone == 0:
        return [1]
    elif stone > 1 and number_of_digits % 2 == 0:
        # split number into two equal parts
        # 1234 becomes 12 and 34
        # 1000 becomes 10 and 0
        # ceil log10 gives number of digits.
        # so by dividing by 10 ** number of digits we get the first half if
        # we ignore everything behind the decimal point
        divisor = 10 ** (number_of_digits // 2)
        return [stone // divisor, stone % divisor]
    else:
        return [stone * 2024]

def precalc_number(iterations, number):
    stones = [number]
    precalced_values = []
    for i in range(iterations):
        print(f'Precalc iterations: {i}')
        idx = 0
        to_append = []
        while idx < len(stones):
            new_stones = apply_rules(stones[idx])
            if len(new_stones) == 2:
                to_append.append(new_stones[1])
            stones[idx] = new_stones[0]
            idx += 1
        stones += to_append
        precalced_values.append(len(stones))
    return precalced_values[::-1]

def iterate_stones(iterations, stones):
    precalced_numbers = {
        0: precalc_number(iterations, 0),
        1: precalc_number(iterations, 1),
        # 24: precalc_number(iterations, 24),
        # 40: precalc_number(iterations, 40),
        # 80: precalc_number(iterations, 80),
    }
    print(precalced_numbers )
    from_precalc = 0
    for i in range(iterations):
        print(f'Iteration {i}')
        # if len(stones) < 40: print(stones)
        idx = 0
        to_append = []
        while idx < len(stones):
            if stones[idx] in precalced_numbers:
                from_precalc += precalced_numbers[stones[idx]][i]
                del stones[idx]
                if idx >= len(stones): break
            new_stones = apply_rules(stones[idx])
            if len(new_stones) == 2:
                to_append.append(new_stones[1])
            stones[idx] = new_stones[0]
            idx += 1
        stones += to_append
    return len(stones) + from_precalc

start_time = time()
print(f'Part 1: {iterate_stones(25, deepcopy(stones))}')
print(f'Execution time: {time() - start_time}')
start_time = time()
print(f'Part 2: {len(iterate_stones(75, deepcopy(stones)))}')
print(f'Execution time: {time() - start_time}')

# cProfile.run('iterate_stones(25, deepcopy(stones))', 'profile')
# p = pstats.Stats('profile')
# p.strip_dirs().sort_stats(-1).print_stats()