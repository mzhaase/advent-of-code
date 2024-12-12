import networkx as nx

from matplotlib import pyplot as plt

"""
Given a map of text, find regions of the same character, calculate the area
of each region as well as the perimeter
"""


debug = False

plot_map = {}
with open('./input', 'r') as f:
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            plot_map[x,y] = char

G = nx.Graph()

def add_neighbors_to_graph(x, y):
    """For a given node, add all its four neighbors to the graph

    Args:
        x (int): x_coordinate of the node
        y (int): y_coordinate of the node
    """
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if (new_x, new_y) in plot_map:
            if plot_map[new_x, new_y] == plot_map[x,y]:
                G.add_edge((x, y), (new_x, new_y))

def calculate_perimeter(component):
    """For a set of x,y coordinates, calculate the perimeter of the region

    Args:
        component (set): Set of x,y tuples
    """
    perimeter = 0
    for node in component:
        _ = 4
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = node[0] + dx, node[1] + dy
            if (new_x, new_y) in component:
                _ -= 1
        perimeter += _
    return perimeter

def count_corners(c):
    """For a set of x,y tuples, count the number of "corners"

    Args:
        c (set): Set of (x,y) tuples
    """
    corners = 0
    for x,y in c:
        # basically checks all cases in which there is a corner
        corners += (x-1, y) not in c and (x, y-1) not in c
        corners += (x+1, y) not in c and (x, y-1) not in c
        corners += (x-1, y) not in c and (x, y+1) not in c
        corners += (x+1, y) not in c and (x, y+1) not in c

        corners += (x - 1, y) in c and (x, y - 1) in c and (x - 1, y - 1) not in c
        corners += (x + 1, y) in c and (x, y - 1) in c and (x + 1, y - 1) not in c
        corners += (x - 1, y) in c and (x, y + 1) in c and (x - 1, y + 1) not in c
        corners += (x + 1, y) in c and (x, y + 1) in c and (x + 1, y + 1) not in c
    return corners

for x,y in plot_map.keys():
    G.add_node((x,y))
    add_neighbors_to_graph(x,y)

ans1 = 0
ans2 = 0
for component in nx.connected_components(G):
    ans1 += len(component) * calculate_perimeter(component)
    ans2 += len(component) * count_corners(component)

print(f'Part 1 answer: {ans1}')
print(f'Part 2 answer: {ans2}')


if debug:
    # plot graph G
    pos = {node: node for node in G.nodes()}
    nx.draw(G, pos, with_labels=False)
    plt.gca().invert_yaxis()
    plt.show()