import sys
sys.setrecursionlimit(10**6)

f = open('input/12.txt', 'r')
garden = [list(x) for x in f.read().splitlines()]
plot_map = dict()
for r_idx, row in enumerate(garden):
    for c_idx, col in enumerate(row):
        plot_map[(r_idx, c_idx)] = col

total = 0
directions = [[0, +1], [0, -1], [+1, 0], [-1, 0]]

# Iterate over all points, removing points as we recognize them as parts of a plot
while len(plot_map) > 0:

    # Store locations for this plot in a list
    locations = [next(iter(plot_map.keys()))]
    i = 0

    # Iterate over the list of locations, checking for adjacent neighbors and adding them to the
    # plot locations list, which then checks for neighbors, etc
    while i < len(locations):
        for dir in directions:
            neighbor_coordinates = tuple([locations[i][0] + dir[0], locations[i][1] + dir[1]])
            neighbor = plot_map.get(neighbor_coordinates)
            if neighbor == plot_map[locations[0]] and neighbor_coordinates not in locations:
                locations.append(neighbor_coordinates)
        i += 1

    # Define area and maximum permieter
    area = len(locations)
    perimeter = 4 * len(locations)

    # If we find a neighbor on an edge of ours, that's 1 edge that is not contributing to the
    # perimeter of this plot. Decrement the perimiter by 1.
    for location in locations:
        for dir in directions:
            neighbor = plot_map.get((location[0] + dir[0], location[1] + dir[1]))
            if neighbor == plot_map[locations[0]]:
                perimeter -= 1

    total += (area * perimeter)

    # Remove all locations for this plot from the original plot map
    for location in locations:
        del(plot_map[location])

print(f'Part 1: {total}')