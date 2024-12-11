import sys
import itertools
from dataclasses import dataclass
from aoclib import grid_helper
sys.setrecursionlimit(10**6)

f = open('input/10.txt', 'r')
topo_map = [[y for y in x] for x in f.read().splitlines()]

# Find all the trailheads in this map
def find_all_trailheads(topo_map) -> list[()]:
    trailheads = []
    for row in range(len(topo_map)):
        for col in range(len(topo_map[row])):
            if topo_map[row][col] == '0':
                trailheads.append((row,col))
    return trailheads

# Tally up the trailhead scores
def score_all_trailheads(trailheads, topo_map) -> int:
    total_score = 0
    for row, col in trailheads:
        found = set()
        score_trailhead(row, col, topo_map, found)
        total_score += len(found)
    return total_score

# Recursive function to find all 9's at a trailhead
def score_trailhead(row, col, topo_map, found):

    value = topo_map[row][col]

    # If we have a garbage value, return
    if value == '.':
        return
    value = int(value)
    # If we made it to a 9, this is a valid trail.  Add this vertex to the set to avoid duplicating 9s
    if value == 9:
        found.add((row, col))
        return found

    # Search all directions for valid paths
    east = grid_helper.get_east(topo_map, col, row)
    west = grid_helper.get_west(topo_map, col, row)
    north = grid_helper.get_north(topo_map, col, row)
    south = grid_helper.get_south(topo_map, col, row)

    if east and east != '.' and int(east) == value+1:
        score_trailhead(row, col+1, topo_map, found)
    if west and west != '.' and int(west) == value+1:
        score_trailhead(row, col-1, topo_map, found)
    if north and north != '.' and int(north) == value+1:
        score_trailhead(row-1, col, topo_map, found)
    if south and south != '.' and int(south) == value+1:
        score_trailhead(row+1, col, topo_map, found)

    return

# Figure out the number of trails that go to a 9
def score_all_trailheads_p2(trailheads, topo_map) -> int:
    total_score = 0
    for row, col in trailheads:
        found = list()
        score_trailhead_p2(row, col, topo_map, found)
        total_score += len(found)
    return total_score

# Recursive function to find all trails from trailhead
def score_trailhead_p2(row, col, topo_map, found):

    value = topo_map[row][col]

    # If we have a garbage value, return
    if value == '.':
        return
    value = int(value)
    # If we made it to a 9, this is a valid trail.  Add this vertex to the set to avoid duplicating 9s
    if value == 9:
        found.append((row, col))
        return found

    # Search all directions for valid paths
    east = grid_helper.get_east(topo_map, col, row)
    west = grid_helper.get_west(topo_map, col, row)
    north = grid_helper.get_north(topo_map, col, row)
    south = grid_helper.get_south(topo_map, col, row)

    if east and east != '.' and int(east) == value+1:
        score_trailhead_p2(row, col+1, topo_map, found)
    if west and west != '.' and int(west) == value+1:
        score_trailhead_p2(row, col-1, topo_map, found)
    if north and north != '.' and int(north) == value+1:
        score_trailhead_p2(row-1, col, topo_map, found)
    if south and south != '.' and int(south) == value+1:
        score_trailhead_p2(row+1, col, topo_map, found)

    return


trailheads = find_all_trailheads(topo_map)
score = score_all_trailheads(trailheads, topo_map)
rating = score_all_trailheads_p2(trailheads, topo_map)
print(f"Part 1: {score}")
print(f"Part 2: {rating}")