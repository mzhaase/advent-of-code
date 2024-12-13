# we need to find a solution to
# X = a_x * a + b_x * b 
# Y = a_y * a + b_y * b
# all numbers are integers
# we can use matrix inversion given that
# A*X = B
# and therefore
# X = A^-1 * B

import re


import numpy as np

ans_1 = 0
ans_2 = 0
with open('input_33209', 'r') as f:
    for line in f:
        if 'Button A' in line:
            a_x, a_y = map(int, re.findall(r'\d+', line))
        elif 'Button B' in line:
            b_x, b_y = map(int, re.findall(r'\d+', line))
        elif 'Prize' in line:
            x, y = map(int, re.findall(r'\d+', line))
        else:
            # create matrices A and B
            A = np.array([[a_x, b_x], [a_y, b_y]])
            B = np.array([x, y])
            C = B + 10000000000000
            
            # solve for X
            X1 = np.linalg.solve(A, B).round()
            X2 = np.linalg.solve(A, C).round()

            # check if the solution actually works, meaning that A*X = B
            if [a_x*X1[0]+b_x*X1[1], a_y*X1[0]+b_y*X1[1]] == [*B]:
                if X1[0] <= 100 and X1[1] <= 100:
                    ans_1 += X1[0] * 3 + X1[1]

            if [a_x*X2[0]+b_x*X2[1], a_y*X2[0]+b_y*X2[1]] == [*C]:
                ans_2 += X2[0] * 3 + X2[1]
print(ans_1)
print(ans_2)