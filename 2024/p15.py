
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
            grid.append([x for x in line.strip()])
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

    for command in commands:
        r_row, r_col = find_robot(grid)
        dir = (0,0)
        match command:
            case '<':
                dir = (0, -1)
            case '^':
                dir = (-1, 0)
            case 'v':
                dir = (+1, 0)
            case '>':
                dir = (0, +1)

        n_pos = grid[r_row + dir[0]][r_col + dir[1]]

        # We've hit a wall - can't move
        if n_pos == '#':
            continue
        # Space is free - move
        elif n_pos == '.':
            grid[r_row][r_col] = '.'
            grid[r_row + dir[0]][r_col + dir[1]] = '@'
        # We need to move boxes (unless it's against a wall
        else:
            # Count how far we go before we can move the boxes
            move_count = 0
            while n_pos != '.' and n_pos != '#':
                move_count += 1
                n_pos = grid[r_row + (dir[0] * move_count)][r_col + (dir[1] * move_count)]

            # if we've hit a wall, we can't do anything - move on
            if n_pos == '#':
                continue
            else:
                # There's a line of boxes at least 1 box long.  Move the rear box to the front
                # and then move the robot to where the rear box was
                grid[r_row][r_col] = '.'
                grid[r_row + dir[0]][r_col + dir[1]] = '@'
                grid[r_row + (dir[0] * move_count)][r_col + (dir[1] * move_count)] = 'O'

grid, commands = parse_input('input/15test.txt')
process_commands(grid, commands)
i = 1
for row in grid:
    print(*row)