from dataclasses import dataclass
from enum import Enum
import json

## Helper Classes
class Orientation(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4

@dataclass
class Guard:
    row: int
    col: int
    orientation: Orientation

## Functions

# Locate the guard inside the patrol area
def find_guard(guard_patrol_area) -> Guard:
    for i in range(len(guard_patrol_area)):
        for j in range(len(guard_patrol_area[0])):
            if guard_patrol_area[i][j] == '^':
                return Guard(i, j, Orientation.Up)

def get_next_position(guard: Guard) -> (int, int):
    new_row = None
    new_col = None
    match guard.orientation:
        case Orientation.Up:
            new_row = guard.row - 1
            new_col = guard.col
        case Orientation.Right:
            new_row = guard.row
            new_col = guard.col + 1
        case Orientation.Down:
            new_row = guard.row + 1
            new_col = guard.col
        case Orientation.Left:
            new_row = guard.row
            new_col = guard.col - 1
    return (new_row, new_col)

def rotate_guard(guard: Guard) -> Guard:
    match guard.orientation:
        case Orientation.Up:
            guard.orientation = Orientation.Right
        case Orientation.Right:
            guard.orientation = Orientation.Down
        case Orientation.Down:
            guard.orientation = Orientation.Left
        case Orientation.Left:
            guard.orientation = Orientation.Up
    return guard

# Process a guard tick
def tick_guard(guard: Guard, guard_patrol_area: [[]], position_set: set, loop_detection_dict=None) -> Guard:


    # Get the new position based on current orientation
    new_row, new_col = get_next_position(guard)

    # If this move takes guard off the map, note as much by returning None
    if new_row < 0 or new_row == len(guard_patrol_area) or new_col < 0 or new_col == len(guard_patrol_area[0]):
        return None

    # Move guard, and mark this new vertex as visited

    # If we've hit an obstacle, rotate 90 degrees, leave position as it is, and let the next tick handle the movement
    # This makes it simpler to handle a case where a guard may hit two obstacles in a row, while it's less efficient
    # than handling the turn + move in a single tick it's easier to reason through (for me anyhow)
    if guard_patrol_area[new_row][new_col] == '#':
        return rotate_guard(guard)

    # At this point we know the guard is 1) not moving off the grid and 2) not hitting an obstruction.
    # So, we move the guard and mark the new vertex as visited
    guard.row = new_row
    guard.col = new_col
    position_set.add((new_row, new_col))

    # part 2 only
    if loop_detection_dict:
        if (new_row, new_col) not in loop_detection_dict:
            loop_detection_dict[(new_row, new_col)] = ((new_row, new_col), guard.orientation)
        elif loop_detection_dict[(new_row, new_col)] == ((new_row, new_col), guard.orientation):
            return Guard(-1,-1,Orientation.Up)

    return guard

# Main program control flow
# Read in data + setup
problem_data = open('input/6.txt', 'r')
patrol_area = [[y for y in x] for x in problem_data.read().splitlines()]
visited_positions = set()

# Find starting guard location
guard = find_guard(patrol_area)
visited_positions.add((guard.row, guard.col))
while guard:
    guard = tick_guard(guard, patrol_area, visited_positions)

print(f"Part 1: {len(visited_positions)}")

# Part 2 - make loops based on dropping #'s in visited squares and running all maps
patrol_dump = json.dumps(patrol_area)
starting_guard = find_guard(patrol_area)
visited_positions.remove((starting_guard.row, starting_guard.col ))
loop_count = 0

for vi, vj in visited_positions:
    starting_guard = find_guard(patrol_area)
    patrol_copy = json.loads(patrol_dump)
    patrol_copy[vi][vj] = '#'
    visited_copy = set()
    loop_detection_dict = {}
    loop_detection_dict[(starting_guard.row, starting_guard.col)] = starting_guard.orientation

    while starting_guard:
        starting_guard = tick_guard(starting_guard, patrol_copy, visited_copy, loop_detection_dict)
        if not starting_guard: ## leaving
            break
        if starting_guard.row == -1:
            loop_count += 1
            break
print(f"Part 2: {loop_count}")