# for a grid of nodes numbered 0-9, find all paths that start from 0 and only
# ever increment by 1 for every step

# idea 1: make a directed graph, whereby the edges always go from smaller to
# bigger node, with weight of a - b, find all 0s, and use Djikstras to calculate
# shortest paths that are of lenght 9
from collections import defaultdict
from time import time as time

import networkx as nx

start_time      = time()
G               = nx.Graph()
map             = {}
coords_by_value = defaultdict(list)

print(f'Init time: {time() - start_time}')
temp_time = time()

# runtime for this: 1 ms
with open('./input', 'r') as f:
    for y, line in enumerate(f):
        for x, node in enumerate(line.strip()):
            value       = int(node)
            map[(x, y)] = value
            coords_by_value[value].append((x, y))

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
            if map[(new_x, new_y)] - map[(x, y)] == 1:
                G.add_edge((x, y), (new_x, new_y))

# runtime: 5 ms
for x, y in map.keys():
    add_neighbors_to_graph(x, y)

print(f'Graph creation time: {time() - temp_time}')
temp_time = time()

# runtime: 71 ms
answer_part_one = 0
answer_part_two = 0
for zero in coords_by_value[0]:
    nines_visited = {}
    paths = nx.all_simple_paths(G, source=zero, target=coords_by_value[9], cutoff=10)
    try:
        for path in paths:
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