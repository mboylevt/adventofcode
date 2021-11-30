import re

def populate_graph(rules):
    graph = {}
    for rule in rules:
        color, quantities = rule.split('bags contain')
        color = color.strip()
        graph[color] = []
        for q in quantities.split(','):
            if q.strip() == "no other bags.":
                continue
            extraction = re.compile(r"(\d+)\s+(\w+\s+\w+)")
            matches = extraction.search(q)
            q_qty = matches.group(1)
            q_color = matches.group(2)
            graph[color].append((q_color, q_qty))
    return graph

def graph_bfs(graph, start, end, path=[]):
    path += [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    for edge in graph[start]:
        color = edge[0]
        qty = edge[1]
        if color not in path:
            newpath = graph_bfs(graph, color, end, path)
            if newpath:
                return path
    return None

# input = open('../data/p7_test_data.txt', 'r')
input = open('../data/p7_data.txt', 'r')
rules = input.readlines()
graph = populate_graph(rules)
target = "shiny gold"
counter = 0
for color in graph.keys():
    if color == target:
        continue
    if graph_bfs(graph, color, target, []):
        counter+=1

print(counter)

i = 1



