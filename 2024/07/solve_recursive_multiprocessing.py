from concurrent.futures import ProcessPoolExecutor
from functools import cache
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

def solve_one(x, values, operator, operators, target):
    if len(values) == 0:
        return x == target
    _ = operators[operator](x, values[0])
    return any([solve_one(_, values[1:], operator, operators, target) for operator in operators.keys()])

def multiprocessing_shim(target, input, operators):
    for operator in operators.keys():
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
print(f'Part 1 solution: {solve_multiprocess(inputs, operators_part_one)}')
print(f'Execution time: {time() - start_time}')
start_time = time()
print(f'Part 2 solution: {solve_multiprocess(inputs, operators_part_two)}')
print(f'Execution time: {time() - start_time}')
