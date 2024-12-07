import itertools

from concurrent.futures import ProcessPoolExecutor
from math import ceil, log10
from time import time as time

# inputs will be a list of tuples, where the first element is the target value
# and the second element is a list of values
inputs = []
with open('./input', 'r') as f:
    for line in f:
        values = list(map(int, line.strip().replace(':','').split(' ')))
        inputs.append((values[0], values[1:]))

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def concatenate(x, y):
    return int(f'{x}{y}')

def concatenate_log(x,y):
    return x * 10**ceil(log10(y+1)) + y

operators_part_one = {
    '+': add,
    '*': multiply
}
operators_part_two = {
    '+': add,
    '*': multiply,
    '|': concatenate_log
}

# multithreading solution
def solve_single(k, values, operators):
    operations = list(itertools.product(operators.keys(), repeat=len(values) - 1))
    for operation in operations:
        for idx, value in enumerate(values):
            if idx == 0:
                _ = value
                continue
            _ = operators[operation[idx - 1]](_, value)
            if _ > k: break
        if _ == k:
            return k
    return 0

def solve_multithread(inputs, operators):
    answer = 0
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(solve_single, k, values, operators) for k, values in inputs]
        for future in futures:
            answer += future.result()
    return answer

start_time = time()
print(f'Part 1 solution: {solve_multithread(inputs, operators_part_one)}')
print(f'Execution time: {time() - start_time}')
start_time = time()
print(f'Part 2 solution: {solve_multithread(inputs, operators_part_two)}')
print(f'Execution time: {time() - start_time}')
