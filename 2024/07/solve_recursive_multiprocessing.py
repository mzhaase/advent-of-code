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

def solve_one(x, values, operator, operators, target):
    if len(values) == 0:
        return x == target

    if operator   == '+': _ = x + values[0]
    elif operator == '*': _ = x * values[0]
    elif operator == '|': _ = x * 10**ceil(log10(values[0] + 1)) + values[0]

    if _ > target:
        return False

    return any([solve_one(_, values[1:], operator, operators, target) for operator in operators])

def multiprocessing_shim(target, input, operators):
    for operator in operators:
        if solve_one(input[0], input[1:], operator, operators, target):
            return target
    return 0

def solve_multiprocess(inputs, operators):
    answer = 0
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(multiprocessing_shim, target, input, operators) for target, input in inputs]
        for future in futures:
            answer += future.result()
    return answer

start_time = time()
ans = solve_multiprocess(inputs, ('+', '*'))
print(f'Part 1 solution: {ans}')
print(f'Execution time: {time() - start_time}')

start_time = time()
ans = solve_multiprocess(inputs, ('+', '*', '|'))
print(f'Part 2 solution: {ans}')
print(f'Execution time: {time() - start_time}')
