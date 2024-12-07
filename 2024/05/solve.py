import networkx as nx
import matplotlib.pyplot as plt

def part_one(rules, updates):
    answer = 0
    incorrect_updates = []
    for update in updates:
        breaks_the_rules = False
        for idx, page in enumerate(update):
            if idx == 0: continue
            if page in rules:
                if any([rule in update[0:idx - 1] for rule in rules[page]]):
                    breaks_the_rules = True
                    incorrect_updates.append(update)
                    break
        if not breaks_the_rules:
            answer += update[int((len(update) - 1) / 2)]
    print(answer)
    return incorrect_updates

def part_two(rules_graph, incorrect_updates):
    answer = 0
    for update in incorrect_updates:
        subgraph        = rules_graph.subgraph(update)
        ordered_update  = list(nx.topological_sort(subgraph))
        answer         += ordered_update[int((len(update) - 1) / 2)]
    print(answer)


rules_graph = nx.DiGraph()
rules = {}
updates = []
with open('./input', 'r') as f:
    for line in f:
        if '|' in line:
            x, y = map(int, line.strip().split('|'))
            if not x in rules:
                rules[x] = []
            rules[x].append(y)
            rules_graph.add_edge(x, y)
        elif ',' in line:
            updates.append(tuple(map(int, line.strip().split(','))))

incorrect_updates = part_one(rules_graph, updates)
part_two(rules_graph, incorrect_updates)