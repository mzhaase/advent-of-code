import re

import numpy as np

aoc = re.findall('(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+)',
                 open('./input_33209').read(), re.S)

def tokens(row):
    ax,ay,bx,by,px,py = map(int, row)
    M = np.array([[ax, bx], [ay, by]])
    P = np.array([px, py])# + 10000000000000
    a,b = map(round, np.linalg.solve(M, P))
    return a*3+b if [a*ax+b*bx,a*ay+b*by]==[*P] else 0

print(sum(map(tokens,aoc)))