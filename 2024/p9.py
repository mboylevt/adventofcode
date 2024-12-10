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
i = 0
while i < len(disk_start):
    test_char = cur_char = disk_start[i]
    cursor = i
    while cur_char == test_char:
        cursor += 1
        if cursor == len(disk_start):
            break
        test_char = disk_start[cursor]
    fsblocks.append(Block(cur_char, cursor-i))
    i = cursor

# print(f'Disk layout: ' + ''.join(disk_start))

compressed_blocks = fsblocks.copy()
reversed_blocks = compressed_blocks.copy()
reversed_blocks.reverse()

outfile = open('out.txt', 'w')
# For all the blocks in reverse order
for moveBlock in reversed_blocks:
    if moveBlock.content == '.':
        continue
    moveBlockIndex = compressed_blocks.index(moveBlock)
    for targetBlockIndex in range(0, len(compressed_blocks)):
        targetBlock = compressed_blocks[targetBlockIndex]

        # If this isn't a free space block (or to the left of the move), then ignore it
        if targetBlock.content != '.' or targetBlockIndex >= moveBlockIndex:
            continue

        # If this is a free space block AND it's large enough to accommodate the move block, move it
        if targetBlock.length >= moveBlock.length:
            resize = False
            # If the target block is bigger than the move block, we need to resize the target block
            # to account for the remaining space
            if targetBlock.length != moveBlock.length:
                targetBlock.length = targetBlock.length - moveBlock.length
                resize = True

            # Remove the old blocks, insert the new ones
            # only add the free space block back if there is space remaining
            del compressed_blocks[moveBlockIndex]
            del compressed_blocks[targetBlockIndex]
            compressed_blocks.insert(targetBlockIndex, moveBlock)
            compressed_blocks.insert(moveBlockIndex, Block('.', moveBlock.length))
            if resize:
                compressed_blocks.insert(targetBlockIndex+1, targetBlock)

            # Do a pass to combine any adjacent .'s
            newlen = len(compressed_blocks)
            i = 0
            while i < newlen-1:
                if compressed_blocks[i].content == compressed_blocks[i+1].content:
                    compressed_blocks[i].length += compressed_blocks[i+1].length
                    del compressed_blocks[i+1]
                    newlen = newlen - 1
                    i = i - 1
                i += 1
            break
        fsmap = ''
        for block in compressed_blocks:
            fsmap += str(block.content * block.length)
        outfile.write(fsmap)


fsmap = ''
for block in compressed_blocks:
    fsmap += str(block.content * block.length)

checksum = 0
for i in range(0, len(fsmap)):
    if fsmap[i] != '.':
        checksum += int(fsmap[i]) * i
print(f'Part 2: {checksum}')