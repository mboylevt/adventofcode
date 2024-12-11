import sys
import itertools
from collections import defaultdict
from dataclasses import dataclass
from aoclib import grid_helper
sys.setrecursionlimit(10**6)

def get_stone_count(starting_stones, depth) -> int:
    stone_count = 0
    # Process each stone individually - this avoids exponential growth in the array
    for starting_stone in starting_stones:
        print(f"Processing stone {starting_stone}")
        stone_array = [int(starting_stone)]
        blinks = 0
        # execute the blink algorithm
        while blinks < depth:
            idx = 0
            while idx < len(stone_array):
                stone = stone_array[idx]
                if stone == 0:
                    stone_array[idx] = 1
                elif len(str(stone)) % 2 == 0:
                    stone_str = str(stone)
                    mid = len(stone_str) // 2
                    half_one = stone_str[0:mid]
                    half_two = stone_str[mid:]
                    stone_array[idx] = int(half_one)
                    stone_array.insert(idx+1, int(half_two))
                    idx += 1
                else:
                    stone_array[idx] = stone * 2024
                idx += 1
            blinks += 1
        stone_count += len(stone_array)
    return stone_count

def calculate_next(val):
    if val == 0:
        return [1]
    if (l:=len(str(val))) % 2 == 0:
        h1 = str(val)[0:l//2]
        h2 = str(val)[l//2:]
        return [int(h1), int(h2)]
    else:
        return [2024*val]

def solve(numbers, blinks):
    nvals = 0

    for index, node in enumerate(numbers):
        last_nodes = {node:1}
        counter = 0

        while counter < blinks:
            new_nodes = defaultdict(int)

            for val, count in last_nodes.items():
                val_next_nodes = calculate_next(val)

                for node in val_next_nodes:
                    new_nodes[node] += count

            last_nodes = new_nodes
            counter += 1
        nvals += sum(last_nodes.values())

    return nvals

f = open('input/11.txt', 'r')
numbers = list(map(int, f.read().splitlines()[0].split(' ')))
print(f'Part 1:{solve(numbers, 25)}')
print(f'Part 2:{solve(numbers, 75)}')