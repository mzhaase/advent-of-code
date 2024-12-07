import re
import timeit

with open('/home/mattis/hobbies/advent-of-code/2024/03/input', 'r') as f:
    content = f.read()

def without_split():
    instruction_re = re.compile(r"(do|don't|mul\((\d{1,3}),(\d{1,3})\))")
    matches = instruction_re.finditer(content)

    sum = 0
    do = True
    for match in matches:
        if match.group(1) == 'do':
            do = True
        elif match.group(1) == 'don\'t':
            do = False
        else:
            if not do: continue
            sum += int(match.group(2)) * int(match.group(3))

    return sum

def with_split():
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")

    # print("Part 1:", sum(int(g[0])*int(g[1]) for g in findall(mul_pattern, data)))
    data = " ".join(part.split("don't()")[0] for part in content.split("do()"))
    return sum(int(g[0])*int(g[1]) for g in re.findall(mul_pattern, data))

print('without_split')
print(timeit.timeit('without_split()', setup="from __main__ import without_split", number=10))
print('with_split')
print(timeit.timeit('with_split()', setup="from __main__ import with_split", number=10))