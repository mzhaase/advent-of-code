# for a grid of nodes numbered 0-9, find all paths that start from 0 and only
# ever increment by 1 for every step

# idea 1: make a directed graph, whereby the edges always go from smaller to
# bigger node, with weight of a - b, find all 0s, and use Djikstras to calculate
# shortest paths that are of lenght 9
import itertools

from time import time as time

import networkx as nx

start_time = time()
G = nx.Graph()

map    = {}
zeroes = []
nines  = []

print(f'Init time: {time() - start_time}')
temp_time = time()

# runtime for this: 1 ms
with open('./input', 'r') as f:
    for y, line in enumerate(f):
        for x, node in enumerate(line.strip()):
            map[(x, y)] = int(node)
            if int(node) == 0:
                zeroes.append((x, y))
            elif int(node) == 9:
                nines.append((x, y))

print(f'Ingest time: {time() - temp_time}')
temp_time = time()

def add_neighbors_to_graph(x, y):
    """For a given node, add all its four neighbors to the graph

    Args:
        x (int): x_coordinate of the node
        y (int): y_coordinate of the node
    """
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if (new_x, new_y) in map:
            node_diff = map[(new_x, new_y)] - map[(x, y)]
            if node_diff == 1:
                G.add_edge((x, y), (new_x, new_y))

# runtime: 5 ms
for x, y in map.keys():
    add_neighbors_to_graph(x, y)

print(f'Graph creation time: {time() - temp_time}')
temp_time = time()

# runtime: 4.4 s
answer_part_one = 0
answer_part_two = 0
for zero in zeroes:
    nines_visited = {}
    for nine in nines:
        paths = nx.all_simple_paths(G, source=zero, target=nine, cutoff=10)
        try:
            for path in paths:
                if len(path) == 10:
                    if not path[9] in nines_visited:
                        nines_visited[path[9]] = True
                        answer_part_one += 1
                answer_part_two += 1
        except nx.NetworkXNoPath:
            continue

print(f'Answer part one: {answer_part_one}')
print(f'Answer part two: {answer_part_two}')
print(f'Answer time: {time() - temp_time}')
print(f'Total time: {time() - start_time}')
