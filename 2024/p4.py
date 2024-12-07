input = open('input/4.txt', 'r')
lines = input.read().splitlines()

def search_east(lines, x, y):
    # if xmas would be past boundary, return 0
    if x + 4 > len(lines[y]):
        return 0
    if lines[y][x+1] == 'M' and lines[y][x + 2] == 'A' and lines[y][x + 3] == 'S':
        return 1
    return 0

def search_southeast(lines, x, y):
    # if xmas would be past boundary, return 0
    if x + 4 > len(lines[y]) or y + 4 > len(lines):
        return 0
    if lines[y+1][x+1] == 'M' and lines[y+2][x+2] == 'A' and lines[y+3][x+3] == 'S':
        return 1
    return 0

def search_south(lines, x, y):
    # if xmas would be past boundary, return 0
    if y + 4 > len(lines):
        return 0
    if lines[y+1][x] == 'M' and lines[y+2][x] == 'A' and lines[y+3][x] == 'S':
        return 1
    return 0

def search_southwest(lines, x, y):
    # if xmas would be past boundary, return 0
    if x - 3 < 0 or y + 4 > len(lines):
        return 0
    if lines[y+1][x-1] == 'M' and lines[y+2][x-2] == 'A' and lines[y+3][x-3] == 'S':
        return 1
    return 0

def search_west(lines, x, y):
    # if xmas would be past boundary, return 0
    if x - 3 < 0:
        return 0
    if lines[y][x-1] == 'M' and lines[y][x-2] == 'A' and lines[y][x-3] == 'S':
        return 1
    return 0

def search_northwest(lines, x, y):
    # if xmas would be past boundary, return 0
    if x - 3 < 0 or y - 3 < 0:
        return 0
    if lines[y-1][x-1] == 'M' and lines[y-2][x-2] == 'A' and lines[y-3][x-3] == 'S':
        return 1
    return 0

def search_north(lines, x, y):
    # if xmas would be past boundary, return 0
    if y - 3 < 0:
        return 0
    if lines[y-1][x] == 'M' and lines[y-2][x] == 'A' and lines[y-3][x] == 'S':
        return 1
    return 0

def search_northeast(lines, x, y):
    # if xmas would be past boundary, return 0
    if y - 3 < 0 or x + 4 > len(lines[y]):
        return 0
    if lines[y-1][x+1] == 'M' and lines[y-2][x+2] == 'A' and lines[y-3][x+3] == 'S':
        return 1
    return 0

def find_all_xmas(lines):
    xmas_count = 0
    for y in range (0, len(lines)):
        for x in range(0, len(lines[y])):
            if lines[y][x] == 'X':
                xmas_count += search_east(lines, x, y)
                xmas_count += search_southeast(lines, x, y)
                xmas_count += search_south(lines, x, y)
                xmas_count += search_southwest(lines, x, y)
                xmas_count += search_west(lines, x, y)
                xmas_count += search_northwest(lines, x, y)
                xmas_count += search_north(lines, x, y)
                xmas_count += search_northeast(lines, x, y)
    return xmas_count

def find_all_x_mas(lines):
    xmas_count = 0
    for y in range (0, len(lines)):
        for x in range(0, len(lines[y])):
            if lines[y][x] == 'A':
                if x == 0 or x == len(lines[y])-1 or y == 0 or y == len(lines)-1:
                    continue
                nw = lines[y-1][x-1]
                sw = lines[y+1][x-1]
                ne = lines[y-1][x+1]
                se = lines[y+1][x+1]
                eval_str = nw + ne + sw + se
                # if nw == 'M' and sw == 'M' and ne == 'S' and se == 'S':
                if eval_str in ('MSMS', 'SSMM', 'SMSM', 'MMSS'):
                    xmas_count += 1

    return xmas_count
print("Part 1: {}".format(find_all_xmas(lines)))
print("Part 2: {}".format(find_all_x_mas(lines)))

