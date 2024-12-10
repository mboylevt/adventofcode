import itertools

problem_data = open('input/8.txt', 'r')
city_grid = [[y for y in x] for x in problem_data.read().splitlines()]

def populate_antenna_map(city_grid):
    antenna_map = dict()
    for i in range(len(city_grid)):
        for j in range(len(city_grid[i])):
            pos_marker = city_grid[i][j]
            if pos_marker != '.':
                if pos_marker not in antenna_map.keys():
                    antenna_map[pos_marker] = [(i, j)]
                else:
                    antenna_map[pos_marker].append((i, j))
    return antenna_map

def determine_distance_between_nodes(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


antenna_map = populate_antenna_map(city_grid) # Get all the antennae
antinodes = set()
antinodes2 = set()

for r in range(len(city_grid)):
    for c in range(len(city_grid[0])):
        for freq, locations in antenna_map.items():
            for (r1, c1) in locations:
                for (r2, c2) in locations:
                    if (r1, c1) != (r2, c2):
                        d1 = abs(r - r1) + abs(c - c1)
                        d2 = abs(r - r2) + abs(c - c2)

                        dr1 = r - r1
                        dr2 = r - r2
                        dc1 = c - c1
                        dc2 = c - c2

                        if(d1 == 2*d2 or d2 == 2*d1) and 0 <= r <= len(city_grid) and 0 <= c <= len(city_grid[0]) and\
                                (dr1 * dc2 == dr2 * dc1):
                            antinodes.add((r, c))
                            # print(f"Adding {(r,c)}")
                        if 0 <= r <= len(city_grid) and 0 <= c <= len(city_grid[0]) and (dr1 * dc2 == dr2 * dc1):
                            antinodes2.add((r, c))
                            # print(f"Adding {(r, c)}")

print(f"Part 1: {len(antinodes)}")
print(f"Part 2: {len(antinodes2)}")