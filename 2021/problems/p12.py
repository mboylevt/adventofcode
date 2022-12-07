from collections import deque
input = open('../data/p12_data.txt', 'r')
# input = open('../data/p12_test_small.txt', 'r')
# input = open('../data/p12_test_big.txt', 'r')
import copy

lines = input.read().split('\n')


def parse_input(lines):
    cave = {}
    for line in lines:
        start, dest = line.split('-')
        if start not in cave.keys():
            cave[start] = []
        if dest not in cave.keys():
            cave[dest] = []
        cave[start].append(dest)
        cave[dest].append(start)
    return cave


def get_paths_1(caves, visited, cave):
    if cave == "end":
        return 1
    generated_paths = 0
    for neigbor in caves[cave]:
        if neigbor not in visited:
            new_visited = visited.copy()
            if neigbor == neigbor.lower():
                new_visited.append(neigbor)
            generated_paths += get_paths_1(caves, new_visited, neigbor)
    return generated_paths


def has_visited_cave(visited, cave):
    if cave == "start":
        return True
    return cave in visited and "twice" in visited


def get_visited_caves(visited_c, cave):
    visited = visited_c.copy()
    is_small = True if cave == cave.lower() else False
    if not is_small:
        return visited
    if cave in visited:
        visited.append("twice")
        return visited
    visited.append(cave)
    return visited

def get_paths_2(caves, visited, cave):
    if cave == "end":
        return 1

    generated_paths = 0
    for neigbor in caves[cave]:
        if not has_visited_cave(visited, neigbor):
            generated_paths += get_paths_2(caves, get_visited_caves(visited, neigbor), neigbor)
    return generated_paths

caves = parse_input(lines)
paths = get_paths_1(caves, ["start"], "start")
print("Part 1: {}".format(paths))
print("Part 2: {}".format(get_paths_2(caves, ["start"], "start")))
