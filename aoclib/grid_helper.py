
def get_east(lines, x, y):
    if x + 1 > len(lines[y]):
        return None
    return lines[y][x+1]

def get_southeast(lines, x, y):
    if x + 1 > len(lines[y]) or y + 1 > len(lines):
        return None
    return lines[y+1][x+1]

def get_south(lines, x, y):
    if y + 1 > len(lines):
        return None
    return lines[y+1][x]

def get_southwest(lines, x, y):
    if x - 1 < 0 or y + 1 > len(lines):
        return None
    return lines[y+1][x-1]

def get_west(lines, x, y):
    if x - 1 < 0:
        return None
    return lines[y][x-1]

def get_northwest(lines, x, y):
    if x - 1 < 0 or y - 1 < 0:
        return None
    return lines[y-1][x-1]

def get_north(lines, x, y):
    if y - 1 < 0:
        return 0
    return lines[y-1][x]

def get_northeast(lines, x, y):
    if y - 1 < 0 or x + 1 > len(lines[y]):
        return None
    return lines[y-1][x+1]