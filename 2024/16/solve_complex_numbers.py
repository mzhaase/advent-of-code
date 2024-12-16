"""
We will use complex numbers to represent coordinates with the real part being
x and the imaginary part being y. This allows us rotations by multiplying with
1j or -1j
"""

import networkx as nx

from matplotlib import pyplot as plt

directions = (1, -1, 1j, -1j)

G = nx.DiGraph()

maze = []
with open('./input', 'r') as f:
    for y, line in enumerate(f):
        maze.append([])
        for x, c in enumerate(line.strip()):
            if c == '#':
                maze[y].append(c)
                continue
            z = y + x * 1j
            # we encode the direction in the node, so every coordinate actually
            # has 4 nodes, one for each direction
            for d in directions:
                G.add_node((z, d))
            # this is just to get a visual representation of the maze
            # to print for debugging and is not part of the solution
            # (except marking start and end positions)
            if c == 'S':
                start = (z, 1j)
                maze[y].append('.')
            elif c == 'E':
                end = z
                maze[y].append('.')
            else:
                maze[y].append(c)

for z, direction in G.nodes:
    if (z + direction, direction) in G.nodes:
        G.add_edge((z, direction), (z + direction, direction), weight=1)
    # using the fact that rotation by 90 degrees is multiplication by 1j or -1j
    # this represents "left" and "right" turns
    for rotation in 1j, -1j:
        G.add_edge((z, direction), (z, direction * rotation), weight=1000)

# we need to also connect the end up
for direction in directions:
    G.add_edge((end, direction), "end", weight=0)

print(f'Part1: {nx.shortest_path_length(G, start, "end", weight='weight')}')

all_shortest_paths = nx.all_shortest_paths(G, start, "end", weight='weight')

nodes = set()
for path in all_shortest_paths:
    for z, direction in path[:-1]:
        nodes.add(z)
print(f'Part2: {len(nodes)}')