input = open('../data/p9_data.txt', 'r')
# input = open('../data/p9_test_data.txt', 'r')
lines = input.read().split()
height_map = [[int(x) for x in y] for y in lines]


def get_adjacent_heights(r, c):
    surrounds = []
    global height_map
    if r > 0: # Can subtract from R
        surrounds.append(height_map[r - 1][c])
    if r < len(height_map) - 1: # Can add to R
        surrounds.append(height_map[r + 1][c])
    if c < len(height_map[0]) - 1: # Can add to C
        surrounds.append(height_map[r][c + 1])
    if c > 0: # can subtract from C
        surrounds.append(height_map[r][c - 1])
    # if r > 0 and c < len(rows[0]) - 1: # Can subtract from R and add to C
    #     surrounds.append(rows[r - 1][c + 1])
    # if r < len(rows) - 1 and c < len(rows[0]) - 1: # Can add to R and C
    #     surrounds.append(rows[r+1][c+1])
    # if r > 0 and c > 0:  # can subtract from R and subtract from C
    #     surrounds.append(rows[r - 1][c - 1])
    # if r < len(rows) - 1 and c > 0:
    #     surrounds.append(rows[r+1][c-1])
    return surrounds

low_points = []
for ridx, row in enumerate(height_map):
    for cidx, val in enumerate(row):
        adjacent_heights = get_adjacent_heights(ridx, cidx)
        min_adjacent = min(adjacent_heights)
        if val < min(adjacent_heights):
            low_points.append(val)

sum = 0
for p in low_points:
    sum += p + 1

print(sum)
