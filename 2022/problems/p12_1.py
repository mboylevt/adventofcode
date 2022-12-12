#!/usr/bin/python3
import fileinput

height = []
start = []
end = []

h = {}
i = 0
for c in 'abcdefghijklmnopqrstuvwxyz':
	h[c] = i
	i += 1
h['S'] = 0
h['E'] = h['z']

row = 0
input = open('../data/p12_data.txt', 'r')
for line in [line for line in input.read().split('\n')]:
	col = 0
	r = []
	for c in line.rstrip():
		r.append(h[c])
		if c == 'S':
			start = [row, col]
		elif c == 'E':
			end = [row, col]
		col += 1
	height.append(r)
	row += 1

# print(height)
# print('Start: %s, End: %s' % (start, end))

# Convert height grid into a Graph of possible moves.
# Only N/S/E/W moves are allowed, and only if the destination height
# is <= 1 + source height.

rows = len(height)
cols = len(height[0])
# print('rows = %d, cols = %d' % (rows, cols))
graph = {}

for r in range(0, rows):
	for c in range(0, cols):
		graph[(r,c)] = []
		# North
		if (r-1 >= 0) and (height[r-1][c] <= 1 + height[r][c]):
			graph[(r,c)].append((r-1,c))
		# South
		if (r+1 < rows) and (height[r+1][c] <= 1 + height[r][c]):
			graph[(r,c)].append((r+1,c))
		# West
		if (c-1 >= 0) and (height[r][c-1] <= 1 + height[r][c]):
			graph[(r,c)].append((r,c-1))
		# East
		if (c+1 < cols) and (height[r][c+1] <= 1 + height[r][c]):
			graph[(r,c)].append((r,c+1))
		# print('r=%d, c=%d, graph(r,c)=%s' % (r, c, graph[(r,c)]))

# BFS algorithm
# borrowed from https://favtutor.com/blogs/breadth-first-search-python
# and https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/breadth-first-search-bfs-algorithm/


def bfs(graph, start, end):
	visited = []
	visited.append(start)
	queue = []
	queue.append(start)
	parent = {}
	parent[start] = None

	found = False
	while queue:
		m = queue.pop(0)
		if m == end:
			found = True
			break

		for neighbor in graph[m]:
			if neighbor not in visited:
				visited.append(neighbor)
				queue.append(neighbor)
				parent[neighbor] = m

	path = []
	if found:
		path.append(end)
		while parent[end] is not None:
			path.append(parent[end])
			end = parent[end]
		path.reverse()
	return path

path = bfs(graph, tuple(start), tuple(end))
print(len(path) - 1)