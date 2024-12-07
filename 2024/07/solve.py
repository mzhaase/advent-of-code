import itertools
from time import time as time

inputs = {}
with open('./input', 'r') as f:
    for line in f:
        values = list(map(int, line.strip().replace(':','').split(' ')))
        inputs[values[0]] = values[1:]

def part_one(inputs):
    answer = 0
    operators = {
        '+': lambda x, y: x + y,
        '*': lambda x, y: x * y
    }
    for k, values in inputs.items():
        operations = permutations = list(itertools.product(operators.keys(), repeat=len(values) - 1))
        for operation in operations:
            for idx, value in enumerate(values):
                if idx == 0:
                    _ = value
                    continue
                _ = operators[operation[idx - 1]]( _, value)
            if _ == k:
                answer += k
                break

    return answer

start_time = time()
print(f'Part 1 solution: {part_one(inputs)}')
print(f'Execution time: {time() - start_time}')