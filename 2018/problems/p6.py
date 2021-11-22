import operator

import numpy as np

class Point():
    def __init__(self, id, xy):
        self.id = id
        self.xy = xy
        self.matrix = None
        self.points = 0
        self.is_infinite = False


points = []
index = 0
with open('../data/p6.data', 'r') as f:
    for line in f.readlines():
        x, y = line.split(',')
        points.append(Point(index, (int(x), int(y))))
        index += 1

data = [map(int, i.split(', ')) for i in open('/home/matt/code/adventofcode/data/p6.data').readlines()]

# Determine matrix size
max_val = 0

for point in points:
    if point.xy[0] > max_val:
        max_val = point.xy[0]
    if point.xy[0] > max_val:
        max_val = point.xy[0]
    if point.xy[1] > max_val:
        max_val = point.xy[1]
    if point.xy[1] > max_val:
        max_val = point.xy[1]

# Populate individual manhattan distances
for point in points:
    area = np.zeros((max_val + 1, max_val + 1))
    for x in range(max_val+1):
        for y in range(max_val + 1):
            manhattan_distance = abs(x - point.xy[0]) + abs(y - point.xy[1])
            area[y, x] = manhattan_distance
    point.matrix = area

# Determine final fabric
final_fabric = np.zeros((max_val + 1, max_val + 1))
for x in range(max_val + 1):
    for y in range(max_val + 1):
        min_val = 100000
        point_id = 0
        for point in points:
            if point.matrix[y][x] == min_val:
                point_id = -1
            if point.matrix[y][x] < min_val:
                min_val = point.matrix[y][x]
                point_id = point.id
        final_fabric[y][x] = point_id

min = 0
max = max_val
exclude = set()
counter = np.zeros(len(points))

# Count final fabric
for x in range(max_val + 1):
    for y in range(max_val + 1):
        if x == max or y == max or x == min or y == min:
            exclude.add(int(final_fabric[y][x]))
        else:
            counter[int(final_fabric[y][x])] += 1

# Filter out infinites
valids = {}
for p in points:
    if p.id not in exclude:
        valids[p.id] = counter[p.id]

print(sorted(valids.items(), key=operator.itemgetter(1))[1])

i = 1

