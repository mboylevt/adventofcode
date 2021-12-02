from collections import Counter
from copy import deepcopy

def get_surrounding_seats(rows, r, c):
    surrounds = []
    if r > 0: # Can subtract from R
        surrounds.append(rows[r - 1][c])
    if r < len(rows) - 1: # Can add to R
        surrounds.append(rows[r + 1][c])
    if c < len(rows[0]) - 1: # Can add to C
        surrounds.append(rows[r][c + 1])
    if c > 0: # can subtract from C
        surrounds.append(rows[r][c - 1])
    if r > 0 and c < len(rows[0]) - 1: # Can subtract from R and add to C
        surrounds.append(rows[r - 1][c + 1])
    if r < len(rows) - 1 and c < len(rows[0]) - 1: # Can add to R and C
        surrounds.append(rows[r+1][c+1])
    if r > 0 and c > 0:  # can subtract from R and subtract from C
        surrounds.append(rows[r - 1][c - 1])
    if r < len(rows) - 1 and c > 0:
        surrounds.append(rows[r+1][c-1])
    return surrounds


def update(rows):
    new_rows = []
    for idx, row in enumerate(rows):
        new_row = ''
        for idy, col in enumerate(row):
            surrounds = get_surrounding_seats(rows, idx, idy)
            if col == '.':
                new_row += '.'
                continue
            elif col == 'L':
                # empty, figure out if full
                if set(surrounds) in ({'L'}, {'.'}, {'L', '.'}):
                    new_row += '#'
                else:
                    new_row += 'L'
            elif col == '#':
                # full, figure out if emtpy
                if Counter(surrounds)['#'] >= 4:
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
