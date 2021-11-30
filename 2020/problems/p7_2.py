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

def graph_dfs(graph, bag_name, bag_count, total=0):
    count = 0
    top_level_bag = graph[node]
    print(f"Currently counting bags inside {bag_name}.")
    print('{} {} -- current total = {}'.format(bag_count, node, total))

    total += bag_count
    for edge in graph[node]:
        color = edge[0]
        qty = int(edge[1])
        total = graph_dfs(graph, color, qty, total)
    return total


def bag_count(bag_collection, bag_name):
    count = 0
    top_level_bag = bag_collection[bag_name]
    print(f"Currently counting bags inside {bag_name}.")

    if len(top_level_bag) == 0:
        return count
    else:
        for (current_bag, qty) in top_level_bag:
            print(f"There are {qty} of {current_bag} inside {bag_name}.")
            # Add the number of bags of the current type
            # to the count.
            current_bag_type_count = int(qty)
            count += current_bag_type_count
            # Count the bags inside each bag of the current type,
            # multiply it by the number of the current type,
            # then add it to the count.
            bags_inside_current_bag_type_count = bag_count(bag_collection, current_bag)
            count += bags_inside_current_bag_type_count * current_bag_type_count

    return count

# input = open('../data/p7_test_data.txt', 'r')
input = open('../data/p7_data.txt', 'r')
rules = input.readlines()
graph = populate_graph(rules)
start = "shiny gold"
# print(graph_dfs(graph, start, 1))
print(bag_count(graph, start))



