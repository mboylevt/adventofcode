input = open('../data/p8_data.txt', 'r')
# input = open('../data/p8_test_data.txt', 'r')
lines = input.read().split()

map = [list(l) for l in lines]
width = len(map[0])
height = len(map)
visible = (2*width) + (2*height) - 4 # All edges are visible, -4 to avoid double-counting corners

def determine_visibility(map, x, y):
    this_tree = map[x][y]
    others = []
    for n in range(0, x):
        others.append(map[n][y])
    if max(others) < this_tree:
        return 1
    others = []
    for s in range(x+1, height):
        others.append(map[s][y])
    if max(others) < this_tree:
        return 1
    others = []
    for e in range(0, y):
        others.append(map[x][e])
    if max(others) < this_tree:
        return 1
    others = []
    for w in range(y+1, width):
        others.append(map[x][w])
    if max(others) < this_tree:
        return 1
    return 0


def determine_scenic_score(map, x, y):
    n_score = s_score = e_score = w_score = 0
    this_tree = map[x][y]

    # North
    for n in range(x - 1, -1, -1):
        n_score += 1
        if map[n][y] >= this_tree:
            break

    # South
    for s in range(x + 1, height):
        s_score += 1
        if map[s][y] >= this_tree:
            break

    # East
    for e in range(y - 1, -1, -1):
        e_score += 1
        if map[x][e] >= this_tree:
            break

    # West
    for w in range(y + 1, width):
        w_score += 1
        if map[x][w] >= this_tree:
            break


    return n_score * s_score * e_score * w_score



# Debugging
# for row in map:
#     print(' '.join(row))

for x in range(1, width-1):
    for y in range (1, height-1):
        is_vis = determine_visibility(map, x, y)
        if is_vis:
            visible += 1
        #     print("Point {} is visible at map {} {}".format(map[x][y],x,y))
        # else:
        #     print("Point {} is NOT visible at map {} {}".format(map[x][y], x, y))
print("part 1: {}".format(visible))

scores = []
for x in range(1, width-1):
    for y in range (1, height-1):
        scores.append(determine_scenic_score(map, x, y))

print("part 2: {}".format(max(scores)))