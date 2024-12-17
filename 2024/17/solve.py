import re

with open('input', 'r') as file:
    text = file.read()

pattern = r"Register A:\s*(\d+)\s*Register B:\s*(\d+)\s*Register C:\s*(\d+)\s*Program:\s*([\d,]+)"
match = re.search(pattern, text)

if match:
    A = int(match.group(1))
    B = int(match.group(2))
    C = int(match.group(3))
    program = list(map(int, match.group(4).split(',')))

def run_program(program, A, B, C):
    pointer = 0
    output  = []
    while True:
        opcode  = program[pointer]
        operand = program[pointer + 1]

        if operand == 4:
            operand = A
        elif operand == 5:
            operand = B
        elif operand == 6:
            operand = C

        if opcode == 0:
            # adv
            A = A // (2 ** operand)
        elif opcode == 1:
            # bxl
            B = B ^ operand
        elif opcode == 2:
            # bst
            B = operand % 8
        elif opcode == 3:
            # jnz
            if A:
                pointer = operand
                continue
        elif opcode == 4:
            # bxc
            B = B ^ C
        elif opcode == 5:
            # out
            output.append(operand % 8)
        elif opcode == 6:
            # bdv
            B = A // (2 ** operand)
        elif opcode == 7:
            # cdv
            C = A // (2 ** operand)
        pointer += 2
        if pointer + 1 >= len(program):
            return output

print('Part 1')
output = run_program(program, A, B, C)
print(','.join(map(str, output)))


print('Part 2')
# we have to find a value for A where the output produced is the program itself
# key insight:
# every element of the output is in a cycle. Cycle length is 1, 8, 64, 512, etc
# so its 2 ** (n*3) where n is the lenght of the program, starting from 0
#
# program is 16 elements long. So we can do 2 ** (16 * 3) increments until the last
# number is correct, then do 2 ** (15 * 3) increments until the second to last
# number is correct, etc


# i know the below kind of does the right thing, but not quite.
# running out of time to debug it.
# probably can do a recursive function trying for every case where the last 
# digit is correct, then the second to last, etc
# because there are some dead branches in the tree of possibilities.
# if j equals a multiple of 8, it will change the digit one level up.
i = 15
j = 1
k = 0
while True:
    A = k + (j * (2 ** (i * 3)))
    output = run_program(program, A, B, C)
    j += 1

    if output == program:
        print(A)
        break

    if output[i] == program[i]:
        i -= 1
        k = A
        j = 1