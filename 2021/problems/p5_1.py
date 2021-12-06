input = open('../data/p5_test_data.txt', 'r')
# input = open('../data/p5_data.txt', 'r')

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "({},{})".format(self.x, self.y)

raw_coords = input.read().split('\n')
max_x = 0
max_y = 0
parsed_coords = []
for line in raw_coords:
    first, second = line.split(' -> ')
    x1, y1 = first.split(',')
    x2, y2 = second.split(',')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    if x1 > max_x:
        max_x = x1
    elif x2 > max_x:
        max_x = x2
    if y1 > max_y:
        max_y = y1
    elif y2 > max_y:
        max_y = y2
    parsed_coords.append([Point(x1, y1), Point(x2, y2)])
point_count = [[0 for x in range(0, max_x+1)] for x in range(0, max_y+1)]

for coodinates in parsed_coords:
    origin = coodinates[0]
    destination = coodinates[1]
    if origin.x != destination.x and origin.y != destination.y:
        continue
    if origin.x == destination.x:
        for y in range(min(origin.y, destination.y), max(origin.y, destination.y) + 1):
            new_coord = Point(origin.x, y)
            point_count[y][origin.x] += 1
    else:
        for x in range(min(origin.x, destination.x), max(origin.x, destination.x)+1):
            new_coord = Point(x, origin.y)
            point_count[origin.y][x] += 1

multi = 0
for ridx, row in enumerate(point_count):
    for cidx, col in enumerate(row):
        if point_count[ridx][cidx] == 0:
            print('.', end='')
        else:
            print(point_count[ridx][cidx], end='')

        if point_count[ridx][cidx] > 1:
            multi+=1
    print()

print(multi)