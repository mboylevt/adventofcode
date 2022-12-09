from collections import deque
input = open('../data/p13_data.txt', 'r')
# input = open('../data/p13_test_data.txt', 'r')
# input = open('../data/p12_test_big.txt', 'r')

# Let's parse
segmented = input.read().split('\n\n')
points = [[int(point.split(',')[0]), int(point.split(',')[1])] for point in segmented[0].split('\n')]
max_row = max(points, key=lambda x: x[0])[0]+1
max_col = max(points, key=lambda x: x[1])[1]+1
instructions = [instruction.split(' ')[2] for instruction in segmented[1].split('\n')]

def fold(paper, instruction):
    [fold_axis, fold_number] = instruction.split('=')
    fold_number = int(fold_number)
    if fold_axis == 'y':
        landing_matrix = paper[:fold_number]
        folding_matrix = paper[fold_number+1:]
        folding_matrix.reverse()
    else:
        landing_matrix = []
        folding_matrix = []
        for row in paper:
            landing_matrix.append(row[:fold_number])
            fold_row = row[fold_number+1:]
            fold_row.reverse()
            folding_matrix.append(fold_row)

    for x in range(0, len(landing_matrix)):
        for y in range(0, len(landing_matrix[0])):
            if folding_matrix[x][y] == '#':
                landing_matrix[x][y] = '#'

    return landing_matrix



# Make yer hashes
paper = [['.'] * max_row for i in range(0, max_col)]
for point in points:
    paper[point[1]][point[0]] = '#'
for row in paper:
    print(' '.join(row))

p1 = True
for instruction in instructions:
    paper = fold(paper, instruction)
    if p1:
        count = 0
        for row in paper:
            for col in row:
                if col == '#':
                    count += 1
        print("Part1: {}".format(count))
        p1 = False

[print(row) for row in paper]


