with open('./input', 'r') as f:
    data = f.read()

print(f'Part 1: {data.count('(') - data.count(')')}')

floor = 0
position = 1
for char in data:
    if char == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(f'Part 2: {position}')
        break
    position += 1