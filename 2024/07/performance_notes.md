Part 2 only:

using naive algorithm:
```
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
```
Using `if _ > k: break`: 18.696s
Not using this line: 20.106s

Using multithreading with ThreadPoolExecutor, with one thread per input: 32s

Using multiprocessing with ProcessPoolExecutor, one thread per input: 2.923s

Instead of doing 'int(f'{x}{y}') for concatenate, one can do `x * 10**ceil(log10(y+1)) + y`. This basically adds an amount of 0s at the end of x that is equal to the length of y, then adding y to it is the same as concatenating. Reduced time to 2.330s.

Using @lru_cache on the add, concatenate and multiply functions actually slows down the code to 2.5s

Single-process using recursive function: 10.7s.
Multi-process with recursive function: 1.7s