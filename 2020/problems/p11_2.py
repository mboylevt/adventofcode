from collections import Counter
from copy import deepcopy


def get_surrounding_seats(rows, r, c):
    surrounds = []
    max_c = len(rows[0])
    max_r = len(rows)

    # N
    tmp_r = r - 1
    tmp_c = c
    while tmp_r >= 0:
        space = rows[tmp_r][tmp_c]
        if space == 'L' or space == '#':
            surrounds.append(space)
            tmp_c = c
            tmp_r = r
            break
        tmp_r -= 1

    # NE
    tmp_r = r - 1
    tmp_c = c + 1
    while tmp_r >= 0 and tmp_c < max_c:
        space = rows[tmp_r][tmp_c]
        if space == 'L' or space == '#':
            surrounds.append(space)
            tmp_c = c
            tmp_r = r
            break
        tmp_r -= 1
        tmp_c += 1

    # E
    tmp_r = r
    tmp_c = c + 1
    while tmp_c < max_c:
        space = rows[tmp_r][tmp_c]
        if space == 'L' or space == '#':
            surrounds.append(space)
            tmp_c = c
            tmp_r = r
            break
        tmp_c += 1

    # SE
    tmp_r = r + 1
    tmp_c = c + 1
    while tmp_r < max_r and tmp_c < max_c:
        space = rows[tmp_r][tmp_c]
        if space == 'L' or space == '#':
            surrounds.append(space)
            tmp_c = c
            tmp_r = r
            break
        tmp_r += 1
        tmp_c += 1

    # S
    tmp_r = r + 1
    tmp_c = c
    while tmp_r < max_r:
        space = rows[tmp_r][tmp_c]
        if space == 'L' or space == '#':
            surrounds.append(space)
            tmp_c = c
            tmp_r = r
            break
        tmp_r += 1

    # SW
    tmp_r = r + 1
    tmp_c = c - 1
    while tmp_r < max_r and tmp_c >= 0:
        space = rows[tmp_r][tmp_c]
        if space == 'L' or space == '#':
            surrounds.append(space)
            tmp_c = c
            tmp_r = r
            break
        tmp_r += 1
        tmp_c -= 1

    # W
    tmp_r = r
    tmp_c = c - 1
    while tmp_c >= 0:
        space = rows[tmp_r][tmp_c]
        if space == 'L' or space == '#':
            surrounds.append(space)
            tmp_c = c
            tmp_r = r
            break
        tmp_c -= 1

    # NW
    tmp_r = r - 1
    tmp_c = c - 1
    while tmp_r >= 0 and tmp_c >= 0:
        space = rows[tmp_r][tmp_c]
        if space == 'L' or space == '#':
            surrounds.append(space)
            tmp_c = c
            tmp_r = r
            break
        tmp_r -= 1
        tmp_c -= 1

    return surrounds


def update(rows):
    new_rows = []
    for idx, row in enumerate(rows):
        new_row = ''
        for idy, col in enumerate(row):
            if col == '.':
                new_row += '.'
                continue
            surrounds = get_surrounding_seats(rows, idx, idy)
            if col == 'L':
                # empty, figure out if full
                if set(surrounds) in ({'L'}, {'.'}, {'L', '.'}):
                    new_row += '#'
                else:
                    new_row += 'L'
            elif col == '#':
                # full, figure out if emtpy
                if Counter(surrounds)['#'] >= 5:
                    new_row += 'L'
                else:
                    new_row += '#'
        new_rows.append(new_row)
    return new_rows

input = open('../data/p11_data.txt', 'r')
# input = open('../data/p11_test_data1.txt', 'r')
starting_rows = input.read().splitlines()
row_length = len(starting_rows[0])
current_rows = starting_rows
while True:
    updated_rows = update(current_rows)
    for row in updated_rows:
        print(row)
    # if we're static, break
    if current_rows == updated_rows:
        break
    current_rows = updated_rows

count = 0
for r in current_rows:
    for c in r:
        if c == '#':
            count += 1

print(count)
