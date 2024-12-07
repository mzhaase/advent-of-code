rows = []
columns = 140 * ['']
plus_diagonals = 280 * ['']
minus_diagonals = 280 * ['']

with open('./input', 'r') as f:
    for row, line in enumerate(f):
        rows.append(line.strip())
        for column, char in enumerate(line.strip()):
            columns[column] += char
            minus_diagonals[column - row if column - row >= 0 else (column - row) * -1 + 140] += char
            plus_diagonals[column + row] += char

patterns = rows + columns + plus_diagonals + minus_diagonals

sum = 0
for pattern in patterns:
    sum += pattern.count('XMAS')
    sum += pattern.count('SAMX')

print(f'Part 1: {sum}')

# Part 2
# possible cases
# 
# M S  M M  S S  S M
#  A    A    A    A
# M S  S S  M M  S M
def is_x_mas(a_row: int, a_column: int) -> bool:
    cases = [
        {
            'M': ((a_row - 1, a_column - 1), (a_row + 1, a_column - 1)),
            'S': ((a_row - 1, a_column + 1), (a_row + 1, a_column + 1))
        },
        {
            'M': ((a_row - 1, a_column - 1), (a_row - 1, a_column + 1)),
            'S': ((a_row + 1, a_column - 1), (a_row + 1, a_column + 1))
        },
        {
            'M': ((a_row + 1, a_column - 1), (a_row + 1, a_column + 1)),
            'S': ((a_row - 1, a_column - 1), (a_row - 1, a_column + 1))
        },
        {
            'M': ((a_row - 1, a_column + 1), (a_row + 1, a_column + 1)),
            'S': ((a_row - 1, a_column - 1), (a_row + 1, a_column - 1))
        }
    ]
    for case in cases:
        if all(rows[row][column] == 'M' for row, column in case['M']) and all(rows[row][column] == 'S' for row, column in case['S']):
            return True
    return False

x_mas_sum = 0 
for row, line in enumerate(rows):
    for column, char in enumerate(line):
        if row == 0 or column == 0: continue
        if row == 139 or column == 139: continue
        if char == 'A':
            if is_x_mas(row, column):
                x_mas_sum += 1

print(f'Part 2: {x_mas_sum}')

# Part 2 alternative solution
# Find "SAM" and "MAS" occurences in the diagonals, and match up with the other
# diagonal



