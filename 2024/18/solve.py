import networkx as nx

from matplotlib import pyplot as plt

fn = 'input'
inputs = {
    'sample': (6,6),
    'input': (70,70)
}

coordinates = []
with open(fn) as f:
    for line in f:
        x, y = line.strip().split(',')
        coordinates.append((int(x), int(y)))



def build_graph(coordinates):
    G = nx.Graph()
    neighbors = [(1,0), (0,1), (-1,0), (0,-1)]
    for x in range(inputs[fn][0] + 1):
        for y in range(inputs[fn][1] + 1):
            for dx, dy in neighbors:
                _x = x + dx
                _y = y + dy
                if (x, y) in coordinates or (_x, _y) in coordinates: continue
                if _x < 0 or _y < 0 or _x > inputs[fn][0] or _y > inputs[fn][1]:
                    continue
                G.add_edge((x,y), (_x, _y))
    return G


# coords for part 1:
if fn == 'sample':
    max_coords = 12
elif fn == 'input':
    max_coords = 1024

G = build_graph(coordinates[:max_coords])
# find the shortest path
shortest_path = nx.shortest_path(G, (0,0), (inputs[fn][0], inputs[fn][1]))
print('Part 1:', len(shortest_path) - 1)

# part 2: find the first coordinate that would block the exit:
for i in range(max_coords, len(coordinates)):
    if coordinates[i] in G.nodes:
        G.remove_node(coordinates[i])
    if not nx.has_path(G, (0,0), (inputs[fn][0], inputs[fn][1])):
        print('Part 2:', coordinates[i])
        break

# print the graph
# node labels have to become position
# pos = {n: n for n in G.nodes}
# # invert y axis
# plt.gca().invert_yaxis()
# nx.draw(G, pos, with_labels=True)
# plt.show()