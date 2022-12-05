from collections import deque
# input = open('../data/p10_data.txt', 'r')
import copy
input = open('../data/p11_test_data.txt', 'r')
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

for row, r_val in enumerate(octipi):
    for col, c_val in enumerate(octipi):
        adj = get_adjacencies(octipi, row, col)
        submatrix = [octipi[r][c] for (r,c) in adj]
        print(submatrix)