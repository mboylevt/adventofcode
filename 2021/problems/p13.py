from collections import deque
# input = open('../data/p13_data.txt', 'r')
input = open('../data/p13_test_data.txt', 'r')
# input = open('../data/p12_test_big.txt', 'r')
import copy

segmented = input.read().split('\n\n')
points = [[int(point.split(',')[0]), int(point.split(',')[1])] for point in segmented[0].split('\n')]

max_row = max(points, key=lambda x: x[0])[0]+1
max_col = max(points, key=lambda x: x[1])[1]+1

paper = [['.'] * max_row for i in range(0, max_col)]
for point in points:
    paper[point[1]][point[0]] = '#'
for row in paper:
    print(' '.join(row))




