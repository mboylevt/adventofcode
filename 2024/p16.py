import re
import sys
from dataclasses import dataclass
from queue import PriorityQueue

sys.setrecursionlimit(10**6)

def parse_input(ifile) -> [[]]:
    f = open(ifile, 'r')
    return [[y for y in x.strip()] for x in f.readlines()]

def find_start_and_end(maze) -> ((), ()):
    start = (0,0)
    end = (0, 0)
    for r_idx, row in enumerate(maze):
        for c_idx, col in enumerate(row):
            if col == 'S':
                start = (r_idx, c_idx)
            elif col == 'E':
                end = (r_idx, c_idx)
    return start, end

# Djikstras strikes again
def find_best_score(maze, start, end):
    directions = [(0,+1), (+1,0), (0,-1), (-1,0)] # (Row, Column): E, S, W, N
    queue = PriorityQueue()
    queue.put((0, start, 0)) #score, position, direction
    visited = set()
    while True:
        current_status = queue.get()
        c_score, c_pos, c_dir = current_status
        visited.add((c_pos, c_dir)) # We've been here before in this orientation
        for i in [0,-1,+1,+2]: #straight, right, left, backwards
            n_dir = (c_dir + i) % 4
            n_r, n_c = directions[n_dir]
            c_r, c_c = c_pos
            r1, c1 = c_r + n_r, c_c + n_c
            if maze[r1][c1] == '#':
                continue
            if ((r1,c1), n_dir) in visited:
                continue
            n_score = c_score + (abs(i)*1000) + 1
            if (r1, c1) == end:
                return n_score
            queue.put( (n_score, (r1, c1), n_dir))

maze = parse_input('input/16.txt')
start, end = find_start_and_end(maze)

best_score = find_best_score(maze, start, end)
print(f'Part 1: {best_score}')

