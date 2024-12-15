
import re
import sys
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

@dataclass
class Robot:
    pos: tuple
    vel: tuple

def parse_input(ifile):
    f = open(ifile, 'r')
    robots = []
    for line in f.readlines():
        pos, vel = line.split(' ')
        pos = pos[2:].strip()
        vel = vel[2:].strip()
        pos_tuple = int(pos.split(',')[0]), int(pos.split(',')[1])
        vel_tuple = int(vel.split(',')[0]), int(vel.split(',')[1])
        robots.append(Robot(pos=pos_tuple, vel=vel_tuple))
    return robots

def update_grid(robots, grid, debug=False, f=None, tick=None):
    for robot in robots:
        if grid[robot.pos[1]][robot.pos[0]] == '.':
            grid[robot.pos[1]][robot.pos[0]] = 1
        else:
            grid[robot.pos[1]][robot.pos[0]] += 1


    if debug:
        if tick > 6510 and tick < 6520:
            ofile.write(f"\nTick {tick}\n")
        for row in grid:
            if f:
                if tick > 6510 and tick < 6520:
                    s_list = [str(x) for x in row]

                    o = ''.join(s_list)
                    f.write(o + '\n')
            else:
                print(*row)

def tick_grid(robots, grid):
    for robot in robots:
        c_pos = robot.pos
        n_pos = (c_pos[0] + robot.vel[0], c_pos[1] + robot.vel[1])

        # Remove the robot from the current grid position, and reset to empty if 0
        grid[c_pos[1]][c_pos[0]] -= 1
        if grid[c_pos[1]][c_pos[0]] == 0:
            grid[c_pos[1]][c_pos[0]] = '.'

        # handle boundary conditions
        if n_pos[0] < 0:
            n_pos = (len(grid[0]) + n_pos[0], n_pos[1])
        elif n_pos[0] >= len(grid[0]):
            n_pos = (n_pos[0] - len(grid[0]), n_pos[1])
        if n_pos[1] < 0:
            n_pos = (n_pos[0], len(grid) + n_pos[1])
        elif n_pos[1] >= len(grid):
            n_pos = (n_pos[0], n_pos[1] - len(grid) )
        robot.pos = n_pos

def score_quadrant(q):
    score = 0
    for r in q:
        for c in r:
            if c != '.':
                score += c
    return score

def score_grid(grid):
    grid_xkerf = (len(grid) // 2)
    grid_ykerf = (len(grid[0]) // 2)
    n = grid[0:grid_xkerf]
    s = grid[grid_xkerf+1:]
    q1 = list()
    q2 = list()
    q3 = list()
    q4 = list()
    for row in n:
        q1.append(row[0:grid_ykerf])
        q2.append(row[grid_ykerf+1:])

    for row in s:
        q3.append(row[0:grid_ykerf])
        q4.append(row[grid_ykerf+1:])

    total_score = 1
    q1s = score_quadrant(q1)
    q2s = score_quadrant(q2)
    q3s = score_quadrant(q3)
    q4s = score_quadrant(q4)

    return q1s * q2s * q3s * q4s

grid = [['.' for x in range(101)] for y in range(103)]
robots = parse_input('input/14.txt')
update_grid(robots, grid)
ofile = open("xmasfinder.txt", '+w')
for x in range(0, 6600):

    tick_grid(robots, grid)
    update_grid(robots, grid, debug=True, f=ofile, tick=x)
    i = 1

print(f'Part 1: {score_grid(grid)}')

