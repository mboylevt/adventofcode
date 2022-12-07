from collections import deque
input = open('../data/p11_data.txt', 'r')
# input = open('../data/p11_test_data2.txt', 'r')
# input = open('../data/p11_test_data.txt', 'r')

import copy
lines = input.read().split('\n')
s_octipi = [[int(x) for x in line] for line in lines]
FLASH_VAL = 9

def energy_plusplus(arr):
    for row, r_val in enumerate(arr):
        for col, c_val in enumerate(arr):
            arr[row][col] += 1
    return arr


def get_adjacencies(arr, row, col):
    adjacencies = []
    max_r = len(arr)-1
    max_c = len(arr[0])-1

    #N
    if row-1 >= 0:
        adjacencies.append((row - 1, col))
    #NE
    if col+1 <= max_c and row-1 >= 0:
        adjacencies.append((row - 1, col + 1))
    #E
    if col+1 <= max_c:
        adjacencies.append((row, col + 1))
    #SE
    if col+1 <= max_c and row+1 <= max_r:
        adjacencies.append((row + 1, col + 1))
    #S
    if row+1 <= max_r:
        adjacencies.append((row + 1, col))
    #SW
    if col-1 >= 0 and row+1 <= max_r:
        adjacencies.append((row + 1, col - 1))
    #W
    if col-1 >= 0:
        adjacencies.append((row, col - 1))
    #NW
    if col-1 >= 0 and row-1 >= 0:
        adjacencies.append((row - 1, col - 1))

    return adjacencies

def flash(arr):
    while True:
        for row, r_val in enumerate(arr):
            for col, c_val in enumerate(arr):
                if c_val > FLASH_VAL:
                    adj = get_adjacencies(arr, r_val, c_val)


octipi = copy.deepcopy(s_octipi)
# octipi = energy_plusplus(arr=octipi)

# Part 1
flash_count = 0
for cycle in range(0,100):
    energy_plusplus(octipi)
    resolved = False
    while not resolved: # Resolved is true once a full matrix scan has been done w/ no 10's found
        resolved = True # we've not found any 10's
        for row, r_val in enumerate(octipi):
            for col, c_val in enumerate(octipi):
                if octipi[row][col] > 9:
                    resolved = False # we found one
                    flash_count += 1
                    octipi[row][col] = 0
                    adj = get_adjacencies(octipi, row, col) # Get all adjacent row/col values to be inc'd
                    for a in adj:
                        if octipi[a[0]][a[1]] != 0:
                            octipi[a[0]][a[1]] += 1
print("Total Flashes: {}".format(flash_count))

# Part 2
while True:
    this_flashcount = 0
    energy_plusplus(octipi)
    resolved = False
    while not resolved: # Resolved is true once a full matrix scan has been done w/ no 10's found
        resolved = True # we've not found any 10's
        for row, r_val in enumerate(octipi):
            for col, c_val in enumerate(octipi):
                if octipi[row][col] > 9:
                    resolved = False # we found one
                    flash_count += 1
                    this_flashcount += 1
                    octipi[row][col] = 0
                    adj = get_adjacencies(octipi, row, col) # Get all adjacent row/col values to be inc'd
                    for a in adj:
                        if octipi[a[0]][a[1]] != 0:
                            octipi[a[0]][a[1]] += 1
        if this_flashcount >= 100:
            print("Synchronized: {}".format(cycle+1))
            exit(1)