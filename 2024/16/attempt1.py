import networkx as nx

from matplotlib import pyplot as plt

"""
Given a maze, find the shortes path from start to end. Straight movements have a
cost of 1, 90° turns have a cost of 1000.
"""
maze = []
with open('./sample_21148', 'r') as f:
    for y, line in enumerate(f):
        maze.append([])
        for x, c in enumerate(line.strip()):
            if c == 'S':
                start = (x, y)
                maze[y].append('.')
            elif c == 'E':
                end = (x, y)
                maze[y].append('.')
            else:
                maze[y].append(c)

G = nx.Graph()


# first, make a graph with all edges weight 1
for y in range(len(maze)):
    for x in range(len(maze[0])):
        if not maze[y][x] == '.': continue
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= x + dx < len(maze[0]) and 0 <= y + dy < len(maze):
                if maze[y + dy][x + dx] == '.':
                    G.add_edge((x, y), (x + dx, y + dy), weight=1)

pos = {node: node for node in G.nodes}
# rotate y axis
plt.gca().invert_yaxis()
nx.draw(G, pos, with_labels=False)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()
# next, find all corners that exist in the graph
# there are these cases
# .   . .. .. ...  .  .   .  .
# .. ..  . .   .  ... .. .. ...
#                     .   .  .
# we then
# - remove all edges between all nodes in the corner
# - add "diagonal" edges that have weight 1002
# - add "jumping" edges that have weight 2

# data structure:
# sig: nodes that have to be there for the corner type to exist
# diagonal: nodes that have to be removed and replaced with a diagonal edge
# jumping: nodes that have to be removed and replaced with a jumping edge
corner_cases = [
    {
        'sig': ((0, -1), (0, 1), (1, 0), (-1, 0)),
        'diagonal':[
            ((0, -1), (1, 0)),
            ((0, 1), (1, 0)),
            ((0, -1), (-1, 0)),
            ((0, 1), (-1, 0))
        ],
        'jumping': [
            ((0, -1), (0, 1)),
            ((1, 0), (-1, 0))
        ]
    },
    {
        'sig': ((-1, 0), (1, 0), (0, 1)),
        'diagonal': [
            ((-1, 0), (1, 0)),
            ((-1, 0), (0, 1))
        ],
        'jumping': [
            ((1, 0), (0, 1))
        ]
    },
    {
        'sig': ((-1, 0), (1, 0), (0, -1)),
        'diagonal': [
            ((-1, 0), (1, 0)),
            ((-1, 0), (0, -1))
        ],
        'jumping': [((1, 0), (0, -1))]
    },
    {
        'sig': ((0, -1), (0, 1), (1, 0)),
        'diagonal': [
            ((0, -1), (1, 0)),
            ((0, 1), (1, 0))
        ],
        'jumping': [((0, -1), (0, 1))]
    },
    {
        'sig': ((0, -1), (0, 1), (-1, 0)),
        'diagonal': [
            ((0, -1), (-1, 0)),
            ((0, 1), (-1, 0))
        ],
        'jumping': [((0, -1), (0, 1))]
    },
    {
        'sig': ((0, -1), (1, 0)),
        'diagonal': [((0, -1), (1, 0))],
        'jumping': ()
    },
    {
        'sig': ((0, -1), (-1, 0)),
        'diagonal': [((0, -1), (-1, 0))],
        'jumping': ()
    },
    {
        'sig': ((-1, 0), (0, 1)),
        'diagonal': [((-1, 0), (0, 1))], 
        'jumping': ()
    },
    {
        'sig': ((0, 1), (1, 0)),
        'diagonal': [((0, 1), (1, 0))],
        'jumping': ()
    },
]

for y in range(len(maze)):
    for x in range(len(maze[0])):
        if not (x, y) in G.nodes: continue
        if (x, y) == start or (x, y) == end: continue
        for case in corner_cases:
            # detect which corner case we are in
            if all((x + dx, y + dy) in G.nodes for dx, dy in case['sig']):
                # make sure we don't touch start and end
                if any((x + dx, y + dy) == start or (x + dx, y + dy) == end for dx, dy in case['sig']):
                    continue
                for dx, dy in case['sig']:
                    G.remove_edge((x, y), (x + dx, y + dy))
                for node1, node2 in case['diagonal']:
                    dx1, dy1 = node1
                    dx2, dy2 = node2
                    G.add_edge((x + dx1, y + dy1), (x + dx2, y + dy2), weight=1002)
                for node1, node2 in case['jumping']:
                    dx1, dy1 = node1
                    dx2, dy2 = node2
                    G.add_edge((x + dx1, y + dy1), (x + dx2, y + dy2), weight=2)
                break



# plot the graph showing the weights of all the edges, with the node label being
# x, y coordiantes of the nodes
pos = {node: node for node in G.nodes}
# rotate y axis
plt.gca().invert_yaxis()
nx.draw(G, pos, with_labels=False)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()

print(nx.shortest_path_length(G, start, end, weight='weight'))
shortest_path = nx.shortest_path(G, start, end, weight='weight')

# Draw the path and the maze
for y in range(len(maze)):
    for x in range(len(maze[0])):
        if (x, y) in shortest_path:
            if (x, y) == shortest_path[0]:
                print('S', end='')
            elif (x, y) == shortest_path[-1]:
                print('E', end='')
            else:
                print('*', end='')
        else:
            print(maze[y][x], end='')
    print()
