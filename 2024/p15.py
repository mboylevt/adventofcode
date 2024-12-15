
import re
import sys
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

def parse_input(ifile) -> (list, str):
    f = open(ifile, 'r')
    grid = []
    directions = ''
    cmd_start = 0
    for line in f.readlines():
        if line[0] == '#':
            grid.append(line.strip())
            cmd_start += 1
        elif line == '':
            continue
        else:
            directions = line
    return grid, directions

def find_robot(grid) -> (int, int):
    for r_idx, row in enumerate(grid):
        for c_idx, col in enumerate(row):
            if col == '@':
                return r_idx, c_idx


def process_commands(grid, commands):
    r_row, r_col = find_robot(grid)
    for command in commands:
        pass

grid, commands = parse_input('input/15test.txt')
process_commands(grid, commands)