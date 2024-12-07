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


def solve(inputs, operators):
    answer = 0
    for target, values in inputs:
        for operator in operators.keys():
            if solve_one(values[0], values[1:], operator, operators, target):
                answer += target
                break
    return answer

start_time = time()
print(f'Part 1 solution: {solve(inputs, operators_part_one)}')
print(f'Execution time: {time() - start_time}')
start_time = time()
print(f'Part 1 solution: {solve(inputs, operators_part_two)}')
print(f'Execution time: {time() - start_time}')