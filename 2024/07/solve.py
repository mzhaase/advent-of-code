import itertools

from time import time as time

debug = False

inputs = []
with open('./input', 'r') as f:
    for line in f:
        values = list(map(int, line.strip().replace(':','').split(' ')))
        inputs.append((values[0], values[1:]))

def solve(inputs, operators):
    answer = 0
    for k, values in inputs:
        operations = list(itertools.product(operators.keys(), repeat=len(values) - 1))
        for operation in operations:
            solution_string = ''
            for idx, value in enumerate(values):
                if idx == 0:
                    _ = value
                    if debug: solution_string += f'{_}'
                    continue
                _ = operators[operation[idx - 1]](_, value)
                if _ > k: break
                if debug: solution_string += f' {operation[idx - 1]} {value}'
            if _ == k:
                if debug: print(f'Found solution {k} = {solution_string}')
                answer += k
                break
    return answer

operators_part_one = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y
}
operators_part_two = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '|': lambda x, y: int(f'{x}{y}')
}


start_time = time()
print(f'Part 1 solution: {solve(inputs, operators_part_one)}')
print(f'Execution time: {time() - start_time}')
start_time = time()
print(f'Part 2 solution: {solve(inputs, operators_part_two)}')
print(f'Execution time: {time() - start_time}')
