from copy import deepcopy
from math import ceil, log10
from time import time as time

with open('./input', 'r') as f:
    stones = [int(i) for i in f.read().strip().split()]

def iterate_stones(iterations, stones):
    for i in range(iterations):
        print(f'Iteration {i}')
        # if len(stones) < 40: print(stones)
        _ = []
        for stone in stones:
            if stone == 0:
                _.append(1)
            elif stone > 1 and ceil(log10(stone + 1)) % 2 == 0:
                # split number into two equal parts
                # 1234 becomes 12 and 34
                # 1000 becomes 10 and 0
                # ceil log10 gives number of digits.
                # so by dividing by 10 ** number of digits we get the first half if
                # we ignore everything behind the decimal point
                divisor = 10 ** (ceil(log10(stone + 1)) // 2)
                _.append(stone // divisor)
                _.append(stone % divisor)
            else:
                _.append(stone * 2024)
        stones = deepcopy(_)
    return stones

start_time = time()
print(f'Part 1: {len(iterate_stones(25, stones))}')
print(f'Execution time: {time() - start_time}')
start_time = time()
print(f'Part 2: {len(iterate_stones(75, stones))}')
print(f'Execution time: {time() - start_time}')