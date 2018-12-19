import networkx as nx
import re
with open('../data/p7.data') as f:
    input = f.readlines()

# Graph Generation
regex = re.compile(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.')
G = nx.DiGraph()
roots = set()
for line in input:
    prereq, target = regex.match(line).groups()
    G.add_edge(prereq, target)

print(''.join(nx.lexicographical_topological_sort(G)))

task_times = []
tasks = []
time = 0
while task_times or G:
    available_tasks = [t for t in G if t not in tasks and G.in_degree(t) == 0]
    if available_tasks and len(task_times) < 5:
        task = min(available_tasks)  # min gets smallest task alphabetically
        task_times.append(ord(task) - 4)
        tasks.append(task)
    else:
        min_time = min(task_times)
        completed = [tasks[i] for i, v in enumerate(task_times) if v == min_time]
        task_times = [v - min_time for v in task_times if v > min_time]
        tasks = [t for t in tasks if t not in completed]
        time += min_time
        G.remove_nodes_from(completed)

print(time)



#
# root = None
# for node, degree in G.in_degree:
#     if degree == 0:
#         root = node
#         break
#     # print("{} : {}".format(node, degree))
#
# print("Root: {}".format(root))
#
# current_nodes = [root]
# processed_nodes = []
#
# while current_nodes is not []:
#     for node in current_nodes:
#         successors = []
#         for s in G.successors(node):
#             successors.append(s)
#
# nx.draw(G)
