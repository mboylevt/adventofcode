import sys
import itertools
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

f = open('input/9.txt', 'r')
disk_input = f.readline()

disk_start = []

counter = 0
for x in list(disk_input):
    counter += 1
    if counter % 2:
        file_counter = [str(int((counter/2)))]
        disk_start.extend(file_counter * int(x))
    else:
        disk_start.extend('.' * int(x))

# print(''.join(disk_start))

# Part 1
# disk_munge = disk_start.copy()
# for n in range(0, disk_munge.count('.')):
#     first_free_index = disk_munge.index('.')
#     last_file_index = -1
#     for i in range(len(disk_munge)-1, 0, -1):
#         if disk_munge[i] != '.':
#             last_file_index = i
#             break
#     disk_munge[first_free_index] = disk_munge[last_file_index]
#     disk_munge[last_file_index] = '.'
#
# running_sum = 0
# for n in range(0, len(disk_munge)):
#     if disk_munge[n] == '.':
#         break
#     running_sum += n * int(disk_munge[n])
#
# print(f'Part 1: {running_sum}')

@dataclass
class Block:
    content: str
    length: int

fsblocks = []
for i in range(len(disk_start)):
